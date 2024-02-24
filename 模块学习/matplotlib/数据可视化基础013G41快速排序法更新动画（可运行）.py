# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:59:44 2018

@author: 高治国
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import copy
 
obj = [49,38,65,97,76,13,27,49]
res = []
 
def fast_sort(ob,start,end):
    # print(ob,start,end)
    if  end - start <= 1:
        return
    # i,j,k = 0,(len(ob)-1),ob[0]
    i,j,k = start,end,ob[start]
    while j-i != 1:
        for j_r in range(j,i,-1):
            j = j_r
            if ob[j_r]<k:
                ob[i],ob[j_r] = ob[j_r],ob[i]
                break
        # print(ob,i,j)
        for i_r in range(i,j):
            i = i_r
            if ob[i_r]>k:
                ob[i_r],ob[j] = ob[j],ob[i_r]
                break
    res.append(copy.deepcopy(ob))  # 这里发现添加进res的list对象是浅拷贝，或者说向数据结构中添加的list都是浅拷贝，需要注意
    if ob[i] == k:
        fast_sort(ob,start,i-1)
        fast_sort(ob,i+1,end)
    else:
        fast_sort(ob,start,j-1)
        fast_sort(ob,j+1,end)
 
fast_sort(obj,0,(len(obj)-1))
print(res)
 
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(0,8)
ax.set_ylim(0,100)
ax.set_xticks(np.linspace(0,8,9))
ax.set_yticks(np.linspace(0,100,11))
ax.grid()
line, = ax.plot([],[],'go')
 
def init():
    line.set_data([], [])
    return line,
 
def update(data):  # update函数参数默认接收其后的函数或是list
    line.set_xdata(np.linspace(0,7,8))
    line.set_ydata(data)
    return line
 
ani = animation.FuncAnimation(fig,update,res,init_func=init,interval=2*1000,repeat=False)



#%matplotlib qt