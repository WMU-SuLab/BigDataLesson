# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:07:13 2018

@author: 高治国
"""
import random

from random import *


random()                             # 随机浮点数:  0.0 <= x < 1.0
 
uniform(2.5, 10.0)                   # 随机浮点数:  2.5 <= x < 10.0

 
randrange(10)                        # 0-9的整数：
 
randrange(0, 101, 2)                 # 0-100的偶数
 
choice(['win', 'lose', 'draw'])      # 从序列随机选择一个元素
 
deck = 'ace two three four'.split()
shuffle(deck)                        # 对序列进行洗牌，改变原序列
deck
 
sample([10, 20, 30, 40, 50], k=4)    # 不改变原序列的抽取指定数目样本，并生成新序列
 
 
# 6次旋转红黑绿轮盘(带权重可重复的取样)，不破坏原序列,weight[18,18,2]
choices(['red', 'black', 'green'], [18, 18, 2], k=6)
 
# 德州扑克计算概率Deal 20 cards without replacement from a deck of 52 playing cards
# and determine the proportion of cards with a ten-value
# (a ten, jack, queen, or king).
import collections
deck = collections.Counter(tens=16, low_cards=36)
seen = sample(list(deck.elements()), k=20)
seen.count('tens') / 20
 
# 模拟概率Estimate the probability of getting 5 or more heads from 7 spins
# of a biased coin that settles on heads 60% of the time.'H'的概率是0.6，“T”的概率是1-0.6
trial = lambda: choices('HT', cum_weights=(0.60, 1.00), k=7).count('H') >= 5
sum(trial() for i in range(10000)) / 10000
 
# Probability of the median of 5 samples being in middle two quartiles
trial = lambda : 2500 <= sorted(choices(range(10000), k=5))[2]  < 7500
sum(trial() for i in range(10000)) / 10000
 
from statistics import mean
from random import choices
 
data = 1, 2, 4, 4, 10
means = sorted(mean(choices(data, k=5)) for i in range(20))  # mean是求平均
print(f'The sample mean of {mean(data):.1f} has a 90% confidence '
      f'interval from {means[1]:.1f} to {means[-2]:.1f}')  # 这里的f用法



import random
  
checkcode = ''
for i in range(4):
    current = random.randrange(0,4)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
        checkcode += str(temp)
print(checkcode)

import random, string
 
 
def gen_random_string(length):
    # 数字的个数随机产生
    num_of_numeric = random.randint(1,length-1)
    # 剩下的都是字母
    num_of_letter = length - num_of_numeric
    # 随机生成数字
    numerics = [random.choice(string.digits) for i in range(num_of_numeric)]
    # 随机生成字母
    letters = [random.choice(string.ascii_letters) for i in range(num_of_letter)]
    # 结合两者
    all_chars = numerics + letters
    # 洗牌
    random.shuffle(all_chars)
    # 生成最终字符串
    result = ''.join([i for i in all_chars])
    return result
 
if __name__ == '__main__':
    print(gen_random_string(64))



