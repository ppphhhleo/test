#!/usr/bin/env python
# coding=utf-8

import jieba
strs = ["我来到北京清华大学", "乒乓球拍卖完了", "中国科学技术大学"]
for str in strs:
    seg_list = jieba.cut(str, use_paddle = True)
    print("Paddle Mode: " + '/'.join(list(seg_list)))
    print(", ".join(seg_list))
seg_list = jieba.cut("他来到了网易杭研大厦")
print(", ".join(seg_list))
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所后在日本京都大学深造")
print(", ".join(seg_list))
