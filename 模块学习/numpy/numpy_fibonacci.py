# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 13:01:25 2018

@author: 高治国
"""
import numpy as np 
import os
import sys

n = np.arange(1, 9)
sqrt5 = np.sqrt(5)
phi = (1 + sqrt5)/2
fibonacci = np.rint((phi**n - (-1/phi)**n)/sqrt5)




#利萨茹曲线由以下参数方程定义： 
#x = A sin(at + n/2) 
#y = B sin(bt)

a = float(sys.argv[1])
b = float(sys.argv[2])
t = np.linspace(-np.pi, np.pi, 201)
x = np.sin(a * t + np.pi/2)
y = np.sin(b * t)
plot(x, y)
show()

#方波可以近似表示为多个正弦波的叠加。事实上，任意一个方波信号都可以用无穷傅里叶级数来表示。

t = np.linspace(-np.pi, np.pi, 201)
k = np.arange(1, float(sys.argv[1]))
k = 2 * k - 1
f = np.zeros_like(t)
#对于一个数组中每个元素都进行的计算，可以直接像使用变量一样，直接对数组做计算就可以了
for i in range(len(t)):
    f[i] = np.sum(np.sin(k * t[i])/k)
f = (4 / np.pi) * f
plot(t, f)
show()

