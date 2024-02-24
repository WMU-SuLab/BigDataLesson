# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:42:44 2018

@author: 高治国
"""

#集合(确定的无序的一组数据)
#基本操作
#创建集合
#空集合
var = set()
print(var,type(var))

#具有数据的集合
var = {'zhangwang','zhangbo','zhanglang'}
print(var,type(var))

#成员检测
result = 'zhangbo' in var
print(result)

result = 'zhangsan' not in var
print(result)

#集合推导式
var = {'蚂蚱','螳螂','蝈蝈','蛐蛐'}

#基本的集合推导式
result = {'*'+i+'*' for i in var}
print(result)

#带有判断条件的集合推导式
result = {i for i in var if i != '蛐蛐'}
print(result)

#多循环集合推导式
colors = {'red','blue','pink'}
sizes = {36,37,38,39}
result = {c + str(s) for c in colors for s in sizes}
print(result)

#集合函数
'''
#add()  向集合中添加元素
girls = {'mf','sl','yj'}
girls.add('xf')
print(girls)

#pop()  随机删除集合中的一个元素
boys = {'bd','zw','jl','zy'}
result = boys.pop()
print(boys)
print(result)

#remove()  删除集合中指定的元素  删除不存在的元素会报错
boys = {'bd','zw','jl','zy'}
boys.remove('zy')
print(boys)

#discard()  删除集合中指定的元素  删除不存在的元素啥都不做
boys = {'bd','zw','jl','zy'}
boys.discard('zy1')
print(boys)

#clear()  清空集合
boys = {'bd','zw','jl','zy'}
boys.clear()
print(boys)

#copy()  复制集合
boys = {'bd','zw','jl','zy'}
newboys = boys.copy()
print(newboys)
'''

#difference() 计算2个集合的差集
dreamers = {'ljl','wc','xy','zb','lsy'}
girls = {'mmf','lsy','syj'}
result = dreamers.difference(girls)# result = a + b
print(result)

#difference_update()  计算2个集合的差集(差集更新操作)
dreamers = {'ljl','wc','xy','zb','lsy'}
girls = {'mmf','lsy','syj'}
dreamers.difference_update(girls)#a = a + b  a += b
print(dreamers)

#union()  并集操作
dreamers = {'ljl','wc','xy','zb','lsy'}
girls = {'mmf','lsy','syj'}
result = dreamers.union(girls)
print(result)

#update()  并集更新操作
dreamers = {'ljl','wc','xy','zb','lsy'}
girls = {'mmf','lsy','syj'}
dreamers.update(girls)
print(dreamers)

#intersection()  计算2个集合的交集
dreamers = {'ljl','wc','xy','zb','lsy'}
girls = {'mmf','lsy','syj'}
result = dreamers.intersection(girls)
print(result)

#intersection_update  交集更新操作
dreamers = {'ljl','wc','xy','zb','lsy'}
girls = {'mmf','lsy','syj'}
dreamers.intersection_update(girls)
print(dreamers)

#超集和子集
boys = {'zzy','yqw','dw','wzc','lyb','wym','chy'}
zoudu = {'wzc','lyb','wym'}
girls = {'lsy','mmf','syj'}

#issuperset()  检测当前集合是否是另一个集合的超集
result = boys.issuperset(zoudu)
print(result)

#issubset()  检测当前集合是否是另一个集合的子集
result = zoudu.issubset(boys)
print(result)

#isdisjoint()  检测2个集合是否不存在交集  存在交集 False
result = boys.isdisjoint(girls)
print(result)

#symmetric_difference()  对称差集
dreamers = {'ljl','wc','xy','zb','lsy'}
girls = {'mmf','lsy','syj'}
result = dreamers.symmetric_difference(girls)
print(result)

#symmetric_difference_update()  对称更新差集
dreamers = {'ljl','wc','xy','zb','lsy'}
girls = {'mmf','lsy','syj'}
dreamers.symmetric_difference_update(girls)
print(dreamers)

#冰冻集合
#冰冻集合是一种特殊的集合类型,也是集合(集合是列表的话,冰冻集合就是元组)
#创建冰冻集合
#一般不会创建空的冰冻集合
var = frozenset()
print(var,type(var))

#带有数据的冰冻集合
var = frozenset(('qs','szx','bjh','acs'))
print(var,type(var))

#成员检测
result = 'szx' in var
print(result)

#遍历冰冻集合
for i in var:
    print(i)

#集合推导式(无法得到冰冻集合,可以得到集合,列表,元组,字典类型)
result = {i for i in var}
print(result,type(result))

#函数
#冰冻集合可以使用集合的函数(不修改集合本身的函数都可以使用)
var = frozenset(('qs','szx','bjh','acs'))

#copy()
result = var.copy()
print(result)

#集合操作  交集,并集,差集,对称差集等  不修改冰冻集合本身就能使用:冰冻集合的操作结果都是冰冻集合
var1 = frozenset(('qs','szx','bjh','acs'))
var2 = {'szx','bjh','lc','wb'}

#冰冻集合操作
result = var1.union(var2)
print(result)

#普通集合操作(冰冻集合是参考集合)
result = var2.union(var1)
print(result)