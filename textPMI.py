#coding=utf-8
__author__ = 'root'
from PMI import *
import os
import math
from extract import extract

if __name__ == '__main__':
    documents = []
    testfile = '/home/mac/Downloads/comments_IR.csv'
    f = open(testfile, 'r')
    data = f.readlines()
    if data is not None:
        for sentences in data:
            extractwords = []
            words = extract(sentences)
            for word in words:
                extractwords.append(word)
                documents.append(set(extractwords))
    pm = PMI(documents)
    pmi = pm.get_pmi()
    print('get PMI already, start sorting...', '\n')
    sorted(pmi.values())
    for p in pmi:
        if pmi[p] > 0.0:
            print (p, pmi[p], ' positive','\n')
        if pmi[p] < 0 :
            print (p, pmi[p], ' negative', '\n')
        if pmi[p] == 0:
            print (p, pmi[p], ' middle ', '\n')
