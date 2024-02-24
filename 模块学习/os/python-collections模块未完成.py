# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:34:22 2018

@author: 高治国
"""

import collections
a = {1: 2, 2: 3}
b = {1: 3, 3: 4, 4: 5}
chains = collections.ChainMap(a, b)
# maps
# 注意maps是个属性，不是一个方法，其改变
print(chains.maps)  # [{1: 2, 2: 3}, {1: 3, 3: 4, 4: 5}]
# get
assert chains.get(1, -1) == 2
# parents
# 从第二个map开始找
assert chains.parents.get(1, -1) == 3
# popitem
assert chains.popitem() == (2, 3)
# pop
# 返回的是value
assert chains.pop(1) == 2
# new_child
assert chains.new_child()
print(chains.maps)  # [{}, {1: 3, 3: 4, 4: 5}]
chains[2] = 1
print(chains.maps)  # [{2: 1}, {1: 3, 3: 4, 4: 5}]
# setdedault
# 如果已经存在key，则不会添加
assert chains.setdefault(1, 10) == 3
# update
chains.update({2: 4, 3: 5})
print(chains.maps)  # [{1: 2, 2: 4, 3: 5}, {1: 3, 3: 4, 4: 5}]
# keys
print(chains.keys())  # KeysView(ChainMap({2: 4, 3: 5}, {1: 3, 3: 4, 4: 5}))
# KeysView 继承了mapping和set
print(2 in chains.keys())  # True
print(len(chains.keys()))  # 4（重复的不算）
# clear
chains.clear()
print(chains.maps)  # [{}, {1: 3, 3: 4, 4: 5}]



