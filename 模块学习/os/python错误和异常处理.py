# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:58:00 2018

@author: 高治国
"""

#常见的异常

class Human:
    #属性
    sex = 'man'
    age = 18

    #方法
    def run(self):
        print('跑啊~~~')

#实例化对象
#zw = Human()
#print(zw.age)

#AttributeError 尝试访问未知的对象属性
#print(zw.color)

#lists = ['qtt','mll','cyy','lss']
#IndexError 索引错误
#print(lists[200])

#dicts = {'ym':'yongmei','bd':'baidong','qw':'qiaowei'}
#KeyError  键错误
#print(dicts['gg'])

#KeyboardInterrupt 用户键盘终止程序运行
#while True:
    #pass

#NameError  变量名错误
#print(conghao)

#IndentationError  缩进错误
#def myfunc():
 #print('111')
  #print('222')

#ZeroDivisionError  除数不能为0
#12/0

#断言语句
#assert 3 < 1


#try...except语法  用于解决程序异常问题

try:
    #此区域内尝试执行某些代码
    girls = ['jiaojiao','lele','feifei']
    #访问不存在的索引
    #print(girls[10])

    #访问不存在的变量
    #print(pa)

#设置当前区域只接受变量名称错误,并且解决
except NameError:#程序出现异常执行的区域
    print('程序[变量名]出现了异常情况!')

#设定当前区域只接受索引错误,并且解决
except IndexError:
    print('程序[索引]出现了异常情况!')

#接受所有异常的区域,并且解决
except:
    print('程序出现了错误!')

#程序没有出现任何异常执行的区域
else:
    print('太好了一个错误都没有')

#无论程序有没有异常都会执行取余
finally:
    print('工作结束,收工走人')

print('++++++++++++')


#异常处理的小例子

try:
    #书写一个列表
    shits = ['ershi','yanshi','bishi','shi']

    #访问不存在的索引
    print(shits[100])

except IndexError as e:#as语法此处的作用是设置一个变量来接受错误的异常信息对象
    #查看错误异常信息
    print(e,type(e))
    #提供异常的解决方案
    print(shits[-1])

try:
    print(pa)
except NameError:
    print('None')


#自定义错误类型和处理

#导入系统模块
import sys

#定义获取信息的函数()文件名,所在函数名,当前行数
def get_head_info():
    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back
    return ( f.f_code.co_filename, f.f_code.co_name, str(f.f_lineno))

#不能为负数的异常类型
class FuShuError(RuntimeError):#自定义异常类需要继承运行时异常类 可以直接或者间接继承Exception类即可
    #添加初始化魔术非法
    def __init__(self,errormsg = '',errorno = '',errorline = '',errorfile = ''):
        #将错误信息存入对象
        self.msg = errormsg#错误信息
        self.no = errorno#错误编号
        self.line = errorline#错误行数
        self.file = errorfile#错误文件

try:
    #设置年龄
    age = -18
    #检测年龄是否合法
    if age < 0:#年龄为负数  异常
        #抛出异常
        raise FuShuError('值为负数',250,get_head_info()[2],__file__)

#接受非负数的异常
except FuShuError as e:
    print(e,type(e))
    print('年龄为负数属于非法数值')
    age = age * -1

except NameError:
    print('变量书写异常')

except:
    print('程序出现异常')

print(age)


#with语法

'''(推荐使用with语法进行文件操作!)
#文件读取操作
#1.打开文件
fp = open('09.txt','r')
#2.读取文件
result = fp.read()
print(result)
#3.关闭文件
fp.close()
'''

"""
#将程序放入try except语法中
try:
    # 1.打开文件
    fp = open('09.txt', 'r')
    # 2.读取文件
    result = fp.read()
    print(result)
    
    #故意报错
    print(babi)
    '''
    #不行
    # 3.关闭文件
    fp.close()
    '''
    
#文件运行出错可以被OSError接受
except OSError:
    print('程序运行出现问题')
    
except NameError:
    print('变量名错误')
'''    
else:#不行
    #3.关闭文件
    fp.close()
'''
'''
finally:#不行
    #3.关闭文件
    fp.close()
'''
"""

#with语法
try:
    #1.打开文件  #3.with会监控文件的使用自动关闭
    with open('09.txt','r') as fp: #相当于  fp = open('09.txt','r')
        #2.读取文件
        result = fp.read()
        print(result)

        print(bibi)

except OSError:
    print('操作文件出错')

except NameError:
    print('变量不存在')