# coding=utf-8
from bottle import get, post, template, request, Bottle, response, redirect
from json import dumps
from twitter_utility import TwitterUtility
import os
import json
from collections import defaultdict


app = Bottle()
twitter_util = None


def setup(conf):
    global app
    global twitter_util

    consumer_key = conf.get('Twitter', 'consumer_key')
    consumer_secret =  conf.get('Twitter', 'consumer_secret')
    twitter_util = TwitterUtility(consumer_key, consumer_secret, 'https://api.twitter.com/oauth/request_token', 'https://api.twitter.com/oauth/authenticate' , 'https://api.twitter.com/oauth/access_token')


@app.get('/')
def homePage():
    session = request.environ.get('beaker.session')
    session['redirect_url'] = '/check_twitter'
    access_token = None
    if 'access_token' in session:
        access_token = session['access_token']
    session.save()
    return template('home', access_token=access_token).replace('\n', '');


###########################################
# Twitter関連
###########################################
@app.get('/login')
def login():
    callback_url = "https://" + os.environ['HTTP_HOST']  + os.path.dirname(os.environ['REQUEST_URI']) + '/auth'
    try:
        url,request_token = twitter_util.get_request_token(callback_url)

        session = request.environ.get('beaker.session')
        if 'access_token' in session:
            session.pop('access_token')
        session['request_token'] = request_token
        session.save()

        redirect(url)
    except Exception, e:
        return e

@app.get('/auth')
def auth():
    if hasattr(request.query, 'denied'):
        if request.query.denied:
            #拒否された
            redirect('/check_twitter/logout')
            return
    session = request.environ.get('beaker.session')
    if not session.has_key('request_token'):
      url = 'https://' + os.environ['HTTP_HOST'] + '/' + os.path.dirname(os.environ['REQUEST_URI']) + '/login'
      redirect(url)
      return
    request_token = session['request_token']
    try:
        access_token = twitter_util.get_access_token(request.query.oauth_token, request.query.oauth_verifier)
        session['access_token'] = access_token
        session.save()
        if 'redirect_url' in session:
            redirect(session['redirect_url'])
        else:
            return session['access_token']
    except Exception, e:
        return e

@app.get('/logout')
def logout():
    session = request.environ.get('beaker.session')
    session.delete()
    redirect("/check_twitter")

