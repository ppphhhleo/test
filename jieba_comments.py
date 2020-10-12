#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function, unicode_literals
import jieba
import csv
import pandas as pd
import sys
import jieba.posseg as pseg
jieba.load_userdict('/home/mac/Downloads/use_dic.txt')

sys.path.append("../")
jieba.enable_paddle()

file_object2 = open('/home/mac/Downloads/comments_IR.csv').read().split('\n')
stopwords = open('/home/mac/Downloads/stop_words.txt').read()
readlist = open('').read()
Rs2 = []
for i in range(len(file_object2)) :
    segresult = []
    result = []
    seg_list = jieba.cut(file_object2[i], use_paddle = True)
    for w in seg_list :
        segresult.append(w)
    for word in segresult :
        if word in stopwords :
            continue
        else :
            result.append(word)
    Rs2.append(result)
file = open('/home/mac/Downloads/word_jieba_withoutstop.csv', 'w')
writer = csv.writer(file)
writer.writerows(Rs2)
file.close()

