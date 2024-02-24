# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:51:50 2018

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
    
    
    
    
    

#时间元组
'''
专门用于保存时间的元组格式(不是标准的元素格式)
用户定义的时间元组:(年,月,日,时,分,秒,周几,一年中的第几天)
系统返回的时间元组:(tm_year=2017,tm_mon=7,tm_mday=4,,tm_hour=9,tm_min=4,tm_sec=21,tm_wday=1,tm_yday=185,tm_isdst=0)
'''

#导入时间模块
import time

#常用的时间值
#timezone 获取当前时区和0时区(本初子午线所在时区) 相差的时间
print(time.timezone)

#altzone() 获取当前时区和0时区(本初子午线所在时区)相差的秒数
print(time.altzone)

#daylight 检测是否是夏令时
print(time.daylight)

#asctime() 将时间元组转化成可读的英文时间格式
ttp = (1970,1,1,0,0,0,0,0,0)
result = time.asctime()
print(result)

#localtime() 通过时间戳获取本地时间元组
result = time.localtime() #当前时间戳
result = time.localtime(0) #指定时间戳
print(result)

#gmtime() 通过时间戳 获取UTC时间元组
#result = time.ctime()#当前时间戳
result = time.ctime(0)#指定时间戳
print(result)

#ctime() 使用时间戳获取当前时区的可读英文时间格式
#result = time.ctime() #当前时间戳    asctime(localtime())
result = time.ctime(0) #指定时间戳    asctime(localtime(0))
print(result)

#mktime()  使用时间元组制作指定时间的时间戳
ttp = (1999,12,23,0,0,0,0,0,0)
result = time.mktime(ttp)
print(result)

#clock() 获取cpu时间(不计算程序的睡眠时间)
result = time.clock()
print(result)

#perf_counter() 计时器函数(计算程序的睡眠时间)
result = time.perf_counter()
print(result)

#sleep() 程序睡眠(暂停)
#time.sleep(5)

#time() 获取当前的本地时间戳
resutl = time.time()
print(result)

#strftime() str froamt time 格式化时间字符串
#1999-12-23  00:00:00

#时间元组
ttp = (1999,12,21,23,15,0,0,0,0)
result = time.strftime('%Y-%m-%d %H-%M-%S',ttp)
print(result)

#strptime()  str parse time 解析格式化时间字符串
#12月21日1999年 00:15:00
#%m月%d日%Y年 %H:%M:%S

result = time.strptime('12月21日1999年 00:15:00','%m月%d日%Y年 %H:%M:%S')
print(result)





#计算程序运行时间
import time
#第一次获取时间
start = time.clock()

#执行一个程序
lists = range(0,1000000)
newlists = [i * 2 for i in lists]

#第二次获取时间
end = time.clock()
#计算程序运行时间
result = end - start
print('程序运行时间为 : {}秒'.format(result))

#版本 > 3.3   程序计时推荐使用perf_counter

import time
#第一次获取时间
start = time.perf_counter()

#执行一个程序
lists = range(0,1000000)
newlists = [i * 2 for i in lists]

#第二次获取时间
end = time.perf_counter()

#计算程序运行时间
result = end - start
print('程序运行时间为：{}秒'.format(result))