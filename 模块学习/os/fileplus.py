# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:40:58 2018

@author: 高治国
"""

#shutil模块 高级文件处理模块
import shutil

#copy() 复制文件
#result = shutil.copy('/home/sy/下载/001','/home/sy/文档/002')
#print(result)

#copy2() 复制文件,保留原有数据信息
#result = shutil.copy2('/home/sy/下载/001','/home/sy/文档/003')
#print(result)

#copyfileobj() 将一个文件的内容拷贝到另一个文件当中
#result = shutil.copyfileobj(open('01.txt','r')),open('02.txt','a')
#print(result)
#copyfile() 将一个文件的内容拷贝到另一个文件当中 copyfileobj(open(,'r'),open(,'w'))
#result = shutil.copyfile('01.txt','02.txt')
#print(result)

#copytree() 复制整个目录
#result = shutil.copytree('/home/sy/PycharmProjects/python3/11.9','/home/sy/my11.9')
#print(result)

#copymode()  拷贝权限
#result = shutil.copymode('/home/sy/文档/canzhao','/home/sy/文档/mode')
#print(result)

#copystat()  拷贝元数据
#result = shutil.copystat('/home/sy/文档/002','/home/sy/文档/stat')
#print(result)

#rmtree()  删除整个目录
#result = shutil.rmtree('/home/sy/下载/py)

#move()  移动文件或者目录
#result = shutil.move('/home/sy/下载/001','/home/sy/文档/001')
#result = shutil.move()

#which()  检测命令文件所在的文件夹
#result = shutil.which('reboot')
#print(result)

#disk_usage()  查看磁盘使用量
result = shutil.disk_usage('/')
print(result)

#make_archive()  制作归档文件(将指定的文件夹归档成一个文件)
#result = shutil.make_archive('/home/sy/下载/guidang','zip','/home/sy/PycharmProjects')
#print(result)

#unpack_archive()  解包归档文件
#result = shutil.unpack_archive('/home/sy/下载/myguidang.zip','/home/sy/文档')
#print(result)

#get_archive_formats() 获取归档允许使用的类型
#result = shutil.get_archive_formats()
#print(result)

#get_unpack_formats()  获取系统解包的文件类型(包含类型对应的后缀)
#result = shutil.get_unpack_formats()
#print(result)


压缩与解压
#zip模块
import zipfile
'''
#压缩操作
#1.创建压缩文件
zp = zipfile.ZipFile('./11.6.zip','w',zipfile.ZIP_STORED,True)
#print(zp)

#2.向压缩文件中添加内容
#zp.write('/home/sy/文档/001','001')
#zp.write('/home/sy/文档/002','00-2')
zp.write('./getdirsize.py','mydir/gdp.py')

#3.关闭压缩文件
zp.close()
'''

#解压缩文件
#1.打开压缩文件
zp = zipfile.ZipFile('./11.6.zip','r')
print(zp)

#2.解压操作
#指定文件
#zp.extract('00-2','/home/sy/下载')
#全部文件
#zp.extractall('./boys')

#3.关闭文件
zp.close()

#tar模块
import tarfile
'''
#1.打开压缩文件
tp = tarfile.open('./07.tar','w:bz2')
print(tp)

#2.添加内容 压缩文件
tp.add('01.py',arcname= '1.py')
tp.add('02.py',arcname= '2.py')
tp.add('01.txt',arcname= 'txt/1.txt')

#3.关闭压缩文件
tp.close()
'''
#解压操作
#1.打开压缩文件
tp = tarfile.open('07.tar','r')

#2.解压文件
#解压所有文件
#tp.extractall('./girls')

#解压指定文件
tp.extract('1.py','/home/sy')

#3.关闭压缩文件
tp.close()