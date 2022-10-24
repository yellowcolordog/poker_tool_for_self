# -*- coding: utf-8 -*-
import os
d = {
    's':'♠',
    'h':'♥',
    'c':'♣',
    'd':'♦'
}

l = []
with open('184种牌面.txt', 'r', encoding='utf-8') as f:
    for flop in f.readlines():
        word = flop[:6]
        new_word = ''
        for w in word:
            new_w = d.get(w,w)
            new_word+=new_w
        l.append(new_word)


l2 = ['A','K','Q','J','T',]
for i in range(9,1,-1):
    l2.append(str(i))

def sort_func(i):
    l = []
    l.append(l2.index(i[0]))
    l.append(l2.index(i[2]))
    l.append(l2.index(i[4]))
    return l
l.sort(key=sort_func,reverse=False)
for flop in l:
    if flop[0] != flop[2]:
        flop = flop[4:]+flop[2:4]+flop[:2]
    os.makedirs(os.path.join('未分类',flop))