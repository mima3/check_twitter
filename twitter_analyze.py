# coding=utf-8
import MeCab
import os
import re
import twitter
from collections import defaultdict
from math import log
import json

class TwitterAnalyzer:
    def __init__(self, api):
        p = ""
        #if dicdir == "":
        #    p = "-u%s" % (usrdicdir)
        #else:
        #    p = " -d%s -u%s" % (dicdir ,usrdicdir)
        self.api = api
        self.mecab = MeCab.Tagger(p)
        self.wordcount = defaultdict(int)


    def Analyze(self, user, count):
        statuses = self.api.GetUserTimeline(screen_name=user, count=200, trim_user=True)
        self.wordcount = defaultdict(int)
        for s in statuses:
            self.morph( s.text.encode('utf-8') )
        ret = []
        i = 0
        for k, v in sorted(self.wordcount.items(), key=lambda x:x[1], reverse=True):
            if i >= count:
                break
            word = k
            word = word.replace("\"","")
            word = word.replace("\'","")
            word = word.replace("\\","\\\\")
            ret.append( {"text":word ,"weight":v} )
            i += 1
        return ret


    def morph(self,text):
        pos = ['名詞'] #'形容詞', '形容動詞','感動詞','副詞','連体詞','名詞','動詞']
        #pos = ['名詞']
        exclude=['RT','TL','sm','#','さん','する','いる','やる','これ','それ','あれ','://','こと','の','そこ','ん','なる','http','co','jp','com']
        node = self.mecab.parseToNode(text)
        while node:
            fs = node.feature.split(",")
            if fs[0] in pos:
                word = (fs[6] != '*' and fs[6] or node.surface)
                word = word.strip()
                if word.isdigit() == False:
                    if len(word)!=1:
                        if word not in exclude:
                            self.wordcount[word] += 1
            node = node.next
