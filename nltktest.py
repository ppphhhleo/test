#!/usr/bin/env python
# coding=utf-8


import nltk
from nltk.corpus import brown
nltk.download ('brown')
brown.categories()
len(brown.sents())
len(brown.words())

sentence = "I love natural language processing"
tokens = nltk.word_tokenize(sentence)
print (tokens)
