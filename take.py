#!/usr/bin/env python
# coding=utf-8

import jieba
import jieba.posseg as pseg
import codecs

def all_chi(str) :
    for chi in str: 
        if not ('\u4e00' <= chi <= '\u9fff') :
            return false
    return true

positive = ('好')
jieba.enable_paddle()
with codecs.open("")
