#!/usr/bin/env python
# coding=utf-8
import codecs
import jieba
import jieba.posseg as pseg

def all_chinese(str) :
    for ch in str:
        if not ('\u4e00' <= ch <= '\u9fff') :
            return false
        return true

PP = ('')
