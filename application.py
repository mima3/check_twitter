# coding=utf-8
from bottle import get, post, template, request, Bottle, response, redirect, abort
from json import dumps
import os
import json
from collections import defaultdict
from twitter_utility import TwitterUtility
from twitter_analyze import TwitterAnalyzer
import twitter

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


@app.get('/analyze_user')
def analyzeUser():
    session = request.environ.get('beaker.session')
    session['redirect_url'] = '/check_twitter/analyze_user'
    access_token = None
    session.save()
    if not 'access_token' in session:
        # ログインしていない場合は、ログインページにリダイレクト
        redirect('/check_twitter/login')
        return
    access_token = session['access_token']
    return template('analyze_user', access_token=access_token).replace('\n', '');


@app.get('/json/analyze_user/<user>')
def analyzeUserJson(user):
    res = {'data' : None, 'result':0, 'error': ''}
    response.content_type = 'application/json;charset=utf-8'
    session = request.environ.get('beaker.session')
    if not 'access_token' in session or not 'request_token' in session:
        # ログインしていない場合は、エラー
        res['result'] = 1
        res['error'] = 'ログインされていません。'
        return json.dumps(res)
    try:
        api = twitter_util.get_api(session['request_token'], session['access_token'])
        if not api:
            # ログインしていない場合は、エラー
            res['result'] = 2
            res['error'] = 'Twitter APIの取得に失敗しました。'
            return json.dumps(res)
        tw = TwitterAnalyzer(api)
        data = tw.AnalyzeUser(user, 300)
        res['data'] = data
        res['user'] = api.GetUser(screen_name=user).AsDict()
        return json.dumps(res)
    except twitter.TwitterError, ex:
        res['result'] = 3
        for item in ex:
            for e in item:
                res['error'] = e['message']
        return json.dumps(res)



@app.get('/analyze_search')
def analyzeSearch():
    session = request.environ.get('beaker.session')
    session['redirect_url'] = '/check_twitter/analyze_search'
    access_token = None
    session.save()
    if not 'access_token' in session:
        # ログインしていない場合は、ログインページにリダイレクト
        redirect('/check_twitter/login')
        return
    access_token = session['access_token']
    return template('analyze_search', access_token=access_token).replace('\n', '');


@app.get('/json/analyze_search')
def analyzeSearchJson():
    keyword = request.query.keyword
    res = {'data' : None, 'result':0, 'error': ''}
    response.content_type = 'application/json;charset=utf-8'
    session = request.environ.get('beaker.session')
    if not 'access_token' in session or not 'request_token' in session:
        # ログインしていない場合は、エラー
        res['result'] = 1
        res['error'] = 'ログインされていません。'
        return json.dumps(res)
    try:
        api = twitter_util.get_api(session['request_token'], session['access_token'])
        if not api:
            # ログインしていない場合は、エラー
            res['result'] = 2
            res['error'] = 'Twitter APIの取得に失敗しました。'
            return json.dumps(res)
        tw = TwitterAnalyzer(api)
        data, statuses = tw.AnalyzeSearch(keyword=keyword, count=300)
        res['data'] = data
        return json.dumps(res)
    except twitter.TwitterError, ex:
        res['result'] = 3
        for item in ex:
            for e in item:
                res['error'] = e['message']
        return json.dumps(res)


@app.get('/analyze_locate')
def analyzeLocate():
    session = request.environ.get('beaker.session')
    session['redirect_url'] = '/check_twitter/analyze_locate'
    access_token = None
    session.save()
    if not 'access_token' in session:
        # ログインしていない場合は、ログインページにリダイレクト
        redirect('/check_twitter/login')
        return
    access_token = session['access_token']
    return template('analyze_locate', access_token=access_token).replace('\n', '');


@app.get('/json/analyze_locate')
def analyzeLocateJson():
    lat = request.query.lat
    lng = request.query.lng
    radius = request.query.radius
    geocode = 'geocode:' + str(lat) + ',' + str(lng) + ',' + radius
    res = {'data' : None, 'result':0, 'error': ''}
    response.content_type = 'application/json;charset=utf-8'
    session = request.environ.get('beaker.session')
    if not 'access_token' in session or not 'request_token' in session:
        # ログインしていない場合は、エラー
        res['result'] = 1
        res['error'] = 'ログインされていません。'
        return json.dumps(res)
    try:
        api = twitter_util.get_api(session['request_token'], session['access_token'])
        if not api:
            # ログインしていない場合は、エラー
            res['result'] = 2
            res['error'] = 'Twitter APIの取得に失敗しました。'
            return json.dumps(res)
        tw = TwitterAnalyzer(api)
        data, statuses = tw.AnalyzeSearch(keyword=geocode, count=300)
        res['data'] = data
        res['statuses'] = statuses
        return json.dumps(res)
    except twitter.TwitterError, ex:
        res['result'] = 3
        for item in ex:
            for e in item:
                res['error'] = e['message']
        return json.dumps(res)
 
 
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

