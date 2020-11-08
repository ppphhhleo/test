#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function, unicode_literals
import jieba
import csv
import pandas as pd
import sys
sys.path.append("../")
import jieba.posseg as pseg
# jieba.load_userdict("use_dic.txt")
jieba.load_userdict('/home/mac/Downloads/use_dic.txt')

def all_chinese(str) :
    for ch in str:
       # if not(ch == [\u4e00-\u9fa5] or ch == [0-9]):
        if not('\u4e00' <= ch <= '\u9fa5' or '0' <= ch <= '9') :
            continue
        else :
            return True

jieba.enable_paddle()


file_object2 = open('/home/mac/Downloads/comments_IR.csv').read().split('\n')
stopwords = open('/home/mac/Downloads/stop_words.txt').read()
# readlist = open('').read()
Rs2 = []
Num = []
for i in range(len(file_object2)) :
    segresult = []
    result = []
    seg_list = jieba.cut(file_object2[i], use_paddle = True)
    for w in seg_list :
        segresult.append(w)
    for word in segresult :
        if word in stopwords :
            continue
        if not all_chinese(word) :
            continue
        else :
            result.append(word)
    Rs2.append(result)  

Numb = {}
for wod in Rs2:
    Numb[wod] = Num.get(wod, 0) + 1
Num = append(Numb)
    
file = openn('home/mac/Downloads/num.csv', 'w')
writer = csv.writer(file)
writer.writerows(Num)
file.close()
file = open('/home/mac/Downloads/word_jieba_zzbd.csv', 'w')
writer = csv.writer(file)
writer.writerows(Rs2)
file.close()



