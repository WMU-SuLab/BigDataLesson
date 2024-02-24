# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:57:23 2018

@author: 高治国
"""

类的常用函数

#issubclass() 检测一个类是否是另外一个或者一组类中的子类

class Father:
    pass
class Mother:
    pass
class LaoWang:
    pass
class Son(Father,Mother):
    pass

#检测
#result = issubclass(Son,Father)
#result = issubclass(Son,Mother)
#result = issubclass(Son,LaoWang)
result = issubclass(Son,(LaoWang,Mother))#检测是否是Mother或者LaoWang的子类
print(result)

#isinstance() 检测某个对象是否是指定类的对象(类型检测)
a = 10
#result = isinstance(a,int)
#result = isinstance(a,float)
result = isinstance(a,(Father,int)) #检测a是否是Father或者int类的对象
print(result)

#hasattr()  检测类和对象是否有指定的成员
class Human:
    #属性
    sex = 'man'
    age = 19
    color = 'yellow'

    #方法
    def __init__(self):
        self.hair = '黑色'

    def eat(self):
        print('吃饭')

wbq = Human()

#result = hasattr(wbq,'sex')
#result = hasattr(wbq,'age')
result = hasattr(wbq,'drink')
print(result)

result = hasattr(Human,'sex')
print(result)

#getattr() 获取对象/类成员的值
#已存在
#result = getattr(wbq,'age') #相当于wbq.age
#不存在
result = getattr(wbq,'weight','90kg') #成员不存在时设置获取的默认值
print(result)

#setattr() 设置对象/类成员的值
print(wbq.age)
setattr(wbq,'age',29) #相当于wbq.age = 29
print(wbq.age)

#delattr() 删除对象/类成员的值
print(wbq.hair)
delattr(wbq,'hair')
#print(wbq.hair)


#类和对象常用的属性
class Animal:
    pass
class Demo:
    pass

class Human(Animal,Demo):
    '''
    这是类的文档,一个人类的类
    介绍
    成员
    方法
    '''
    #属性
    sex = 'man'
    age = 18
    color = 'yellow'

    #方法
    def sleep(self):
        print('睡觉')

    def hit(self):
        print('打豆豆')

dd = Human()
#__dict__获取对象或者类的自身成员
print(Human.__dict__)
print(dd.__dict__)

#__doc__ 获取类的文档
print(Human.__doc__)
print(dd.__doc__)

#__name__ 获取类名 (类来使用对象不行)
print(Human.__name__)

#__bases__ 获取一个类直接继承的所有父类元组
print(Human.__bases__)

#__module__ 获取类的模块名称  __main__ 当前类文件直接执行的文件
print(Human.__module__)