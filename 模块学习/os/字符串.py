# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:49:58 2018

@author: 高治国
"""

#元组(元组也是一组有序数据的组合，和列表唯一的不同是，元组不可修改)
#创建单个元素的元组
#var = (13,)
var = 23,
print(var,type(var))

#元组只能进行访问操作
var = ('yy','bb','dlrb','glnz')
print(var[1])
print(var[-2])

#元组的序列操作
# +
var1 = (1,3,5,7,9)
var2 = (2,4,6,8,10)
result = var1 + var2
print(result)

#列表或者元组具有很多层
girls = (
    (
        ('小赵','小钱'),
        ('小李','小周')
    ),
    (
        ('小吴','小郑'),
        ('小王','小刘')
    )
)
#访问多层元组中的内容
print(girls[1])
print(girls[1][1])
print(girls[1][1][0])

#元组推导式->生成器->不要则不给
var = (1,2,3,4,5,6,7,8,9)
result = (i * 2 for i in var)
print(result)#结果为生成器
for a in result:
    print(a)