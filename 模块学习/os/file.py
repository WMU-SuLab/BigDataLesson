# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:37:23 2018

@author: 高治国
"""

#文件操作(写入文件,读取文件)
#写入文件
#1.打开文件(打开冰箱)
fp = open('test.txt','w')
print(fp,type(fp))

#2.写入文件(把大象塞进去)
fp.write('什么时候你会觉得不再年轻了?')

#3.关闭文件(关上冰箱)
fp.close()

#读取文件
#1.打开文件(打开冰箱)
fp = open('test.txt','r')
#print(fp)

#2.读取文件(把大象拿出来)
txt = fp.read()
print(txt)

#3.关闭文件(把冰箱门关闭)
fp.close()


#文件常用函数
#open() 打开或者新建一个文件
'''
open('文件路径','打开模式')

#基本模式
w   write  写入模式
    1.文件不存在则新建文件,文件已存在,打开并且清空文件
    2.该模式下只能进行写入操作
r   read   读取模式
    1.文件不存在则报错,文件已存在则打开文件,将指针指向文件的开头
    2.该模式下只能进行读取操作
a   append  追加模式
    1.文件不存在则新建文件,文件已存在则打开文件,将指针指向文件结尾
    2.该模式下只能进行写入操作
x   xor   异或模式
    1.文件已存在则报错,文件不存在则新建文件
    2.该模式下只能进行写入操作
#扩展模式(不能单独使用必须和基本模式一起用)
+  plus  增强模式
    可以使得任何基本模式变成读写模式
b  bytes  位模式
    获取数据或者写入数据的类型为bytes类型
'''

#增强模式
fp = open('wangwang.txt','w+')
#写入操作
fp.write('四处张望')
#将指针设置为开头位置
fp.seek(0)
#读取操作
result = fp.read()
print(result)
fp.close()

#bytes模式  涉及到一个bytes的数据类型
content = '喵星人为啥不能作为警猫呢?'
result = content.encode()#编码操作
print(result)

fp = open('miaomiao.txt','wb')
fp.write(result)
fp.close()

fp = open('miaomiao.txt','rb')
result = fp.read()
print(result.decode())#解码操作
fp.close()


#read() 读取文件内容
fp = open('miaomiao.txt','r')
#读取所有内容
#txt = fp.read()

#读取指定个数的字符
txt = fp.read(5)
print(txt)
fp.close()

#write()  写入文件内容
fp = open('miaomiao.txt','w')
fp.write('kqkyhtk')
fp.close()

#readline()  一次读取一行数据
fp = open('question','r')
result = fp.readline()
result = fp.readline()

#读取一行数据的前n个字符
result = fp.readline(5)
print(result)
fp.close()

#readlines()  一次性将文件按行读取到列表当中取
fp = open('question','r')
#读取所有行
result = fp.readlines()

#根据指定的字符长度 读取n行
result = fp.readlines(50)
print(result)
fp.close()

#writelines() 将容器中的数据一次性写入文件
'''
txt = ['一\n','二\n','三\n','四\n'
fp = open('num.txt','w')
fp.writelines(txt)
fp.close()
'''
#truncate()  文件截取操作
#fp = open('num.txt','a')

#这里的长度单位不是字符而是字节
#fp.truncate(2)
#fp.close()

'''
字符:一个独立存在的文字就是一个字符,无论什么语言什么符号
字节:用于存储数据的基本单位
    1TB = 1024GB
    1GB = 1024MB
    1MB = 1024KB
    1KB = 1024B
    1B = 8bytes
字符集：
    基本的英文编码（1个字节）
        ascii码  -> 记录英文和数字及部分符号的编码 （128个）
        扩展ascii码 -> 增加了ascii码的数量（256个）
        
    制作特定语言的编码（2个字节[针对汉字]）
        gb2312编码 -> 存储了5000个常用汉字  
        gb10800编码-> 扩充了汉字数量
        gbk编码 -> 包含了所有汉字
        big5编码 -> 繁体中文编码
    
    制作世界统一编码（3个字节[针对汉字]）
        utf-8      包含世界上绝大部分的文字的编码
        utf-16     包含世界上绝大部分的文字的编码
'''

#文件函数
'''
#tell() 获取文件指针的位置(字节)
fp = open('01.txt','r')

#输出当前指针位置
pos1 = fp.tell()
print(pos1)

#读取内容
result = fp.read()
print(result)

#输出当前指针位置
pos2 = fp.tell()
print(pos2)

fp.close()
'''
#seek() 移动文件指针的位置
fp = open('01.txt','r')
#获取开始文件指针位置
print(fp.tell)
#移动指针
fp.seek(9)
#获取开始文件指针位置
print(fp.tell())
#读取文件
result = fp.read()
print(result)
fp.close()