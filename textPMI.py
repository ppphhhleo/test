#coding=utf-8
__author__ = 'root'
from PMI import *
import os
import math
import time
from extract import extract
import csv

if __name__ == '__main__':
    documents = []
    testfile = '/home/mac/Downloads/comments_IR.csv'
    f = open(testfile, 'r')
    
    print ('[STEP1] READ COMMENTS FILE')
    read_start = time.perf_counter()
    data = f.readlines()
    read_end = time.perf_counter()
    print ('[STEP1] READ COMMENTS FILE DONE! TIME COST:', read_end - read_start)
    
    print ('[STEP2] EXTRACT WORDS')
    extract_start = time.perf_counter()
    if data is not None:
        for sentences in data:
            extractwords = []
            words = extract(sentences)
            for word in words:
                extractwords.append(word)
                documents.append(set(extractwords))
    extract_end = time.perf_counter()
    print ('[STEP2] EXTRACT WORDS DONE! TIME COST ', extract_end - extract_start)
    
    print ('[STEP3] CALCULATE PMI')
    pmi_start = time.perf_counter()
    pm = PMI(documents)
    pmi_end = time.perf_counter()
    print ('[STEP3] CALCULATE PMI DONE! TIME COST ', pmi_end - pmi_start)
    
    pmi = pm.get_pmi()
    
    print('[STEP4] SORT get PMI already, start sorting...')
    sort_pmi = dict(sorted(pmi.items(), key = lambda x:x[1]))
    
    print('positive and negative and middle', '\n')

    for p in sort_pmi :
        if sort_pmi[p] > 0:
            print (p, sort_pmi[p], ' positive','\n')
        if sort_pmi[p] < 0 :
            print (p, sort_pmi[p], ' negative', '\n')
        if sort_pmi[p] == 0:
            print (p, sort_pmi[p], ' middle ', '\n')

    print('...Writing in file...')

    header = ['word', 'SO-PMI']
    with open('/home/mac/Downloads/SORT.csv', 'a', newline = '', encoding = 'utf-8') as f:
        writer = csv.DictWriter(f, fieldnames = header)
        writer.writeheader()
        writer.writerows(sort_pmi)
    '''
    csvfile = file('/home/mac/Downloads/SORT.csv')
    writer = csv.writer(csvfile)
    writer.writerow(['word', 'SO-PMI'])
    list1 = []
    for i in sort_pmi.values() :
        s = turple (list(i.values()))
    list1.append(s)
    writer.writerows(list1)
    '''
    '''
    he = []
    for headers in sort_pmi.keys():
        he.append(headers)
    headers = he

    with open('/home/mac/Downloads/SORT.csv', 'a', newline = '', encoding = 'utf - 8') as f:
        writer = csv.DictWriter(f, fieldnames = headers)
        writer.writeheader()
        writer.writerows(sort_pmi)
    print('Writing in file done!')
    '''


    
