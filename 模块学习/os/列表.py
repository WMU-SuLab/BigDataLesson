# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:48:44 2018

@author: 高治国
"""

#列表(一组有序数据的组合就是列表)

#创建列表
#空列表
var = list()#var = []
print(var,type(var))

#具有多个元素的列表
var = ['风','水','风水']
print(var,type(var))

#基本操作
var = ['地','火','地火']
#访问列表中的元素
print(var[-2])

#修改元素
var[1] = '水'
print(var)

#删除元素
del var[1]
print(var)

#添加元素(不能加)

#序列操作
listvar1 = ['胡一菲','曾小贤','陆展博']
listvar2 = ['林宛瑜','陈美嘉','吕子乔','关谷神奇']

#相加
result = listvar1 + listvar2
print(result)

#相乘操作
result = listvar1 * 2
print(result)

#分片
#result = listvar2[:3]
#result = listvar2[1:]
#result = listvar2[1:3]
#result = listvar2[:]
#print(result)

#成员检测
result = 'Lisa荣' in listvar2
print(result)

result = 'Lisa荣' not in listvar2
print(result)

#序列函数
#len() 检测列表中元素的个数
var = ['张三','李四','王五','赵六']
result = len(var)
print(result)

#max() 获取最大值
result = max([12,23,34,45,21,32,43,54])
print(result)

#min() 获取最小值
result = min([12,23,34,45,21,32,43,54])
print(result)

#遍历列表

#for...in
var = ['红','橙','黄','绿','青','蓝','紫']
for i in var:
    print(i)

#while遍历
i = 0
while i < len(var):
    print(var[i])
    i += 1

#多层列表的遍历
var = [
    ['小黑','black'],
    ['小白','white'],
    ['小彩','color']
]

#等长二级列表
for i,j in var:
    print(i,j)

#等长或不等长列表都可以遍历
for i in var:
    #print(i)
    for j in i:
        print(j)

#列表推导式
var = ['段誉','虚竹','乔峰','木婉清','钟灵儿']
#最基本的列表推导式
result = ['@'+i+'@' for i in var]
print(result)

#书写列表1-10,使用列表推导式获取当前列表中每个数字*3的列表
var = [1,2,3,4,5,6,7,8,9,10]
result = [i * 3 for i in var]
print(result)

#带有判断条件的列表推导式
var = [1,2,3,4,5,6,7,8,9,10]
result = [a for a in var if a % 2 == 0]
print(result)

#声明一个多人名称的列表,使用推导式获取所有三个字人名
var = ['段誉','虚竹','乔峰','木婉清','钟灵儿']
result = [n for n in var if len(n) == 3]
print(result)

#多循环列表推导式
sizes = [37,38,39,40,41]
colors = ['yellow','cyan','pink','purple']
result = [str(s) +'-'+ c for s in sizes for c in colors]
print(result)

#男组4人,女组5人,互相见面一次
men = ['男1','男2','男3','男4']
women = ['女1','女2','女3','女4','女5']
result = [m +'-'+ w for m in men for w in women]
print(result)

#带有判断条件的多循环列表推导式
men = ['男1','男2','男3','男4']
women = ['女1','女2','女3','女4']
result = [m +'-'+ w for m in men for w in women if men.index(m) == women.index(w)]
print(result)


#append()  向列表的末尾添加元素  直接修改元列表
var = ['a','b','c','d']
print(var)
var.append('e')
print(var)

#insert() 在列表的指定位置之前添加元素
var = ['a','b','c','d']
print(var)
var.insert(2,'g')
print(var)

#pop()  删除列表中指定位置的元素
var = ['a','b','c','d']
print(var)
result = var.pop(0)
print(var,result)

#remove()  删除列表中指定值的元素
var = ['a','b','c','d']
print(var)
result = var.remove('c')
print(var,result)

#clear()  清空列表
var = ['a','b','c']
print(var,id(var))
var.clear()
print(var,id(var))

#copy()  复制列表
var = ['a','b','c','d']
print(var,id(var))
newvar = var.copy()
print(newvar,id(newvar))

#count() 计算列表中某个元素出现的次数
var = [2,3,4,3,4,5,6,7,8,5,4,6,7,8]
result = var.count(5)
print(result)

#excend() 将一个列表合并到另外一个列表中
var1 = ['xs','dc','yyh','wzj']
var2 = ['dsn','lss','cyy','lrs']
var1.extend(var2)
print(var1)

#index() 获取某个元素在列表中的索引
var = ['xs','dc','yyh','wzj']
result = var.index('dc')
print(result)

#reverse() 列表反转操作
var = ['a','b','c','d']
print(var)
var.reverse()
print(var)

#sort() 排序函数
var = [23,342,34,32,75,59]

#默认排序  升序
#var.sort()
#print(var)

#降序
#var.sort(reverse=True)
#print(var)

#自定义排序规则
#奇偶数
def myfunc(num):
    result = num % 5
    return result
var.sort(key=myfunc,reverse = True)
print(var)

a = [4,5,66,45,99]
 #   0 1 0 1 1
 #   1 0 1 0 0
#a.sort(key=ceshi,reverse=False)
a.sort(key = lambda x:x%2==0)
#print(a)

def ceshi(x):
    return x%2 == 0
a.sort(key=ceshi)
print(a)

#sort 排序按照返回值来排 特点基于原来列表进行排序
'''
> < >= <= != ==

true 1  false 0

True + 1 1+1
+ 1.1 2.1

bool  int  float
float()
int()
bool()
'''




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