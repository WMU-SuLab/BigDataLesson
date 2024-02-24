# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:44:55 2018

@author: 高治国
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
 
def data_gen():
    t = 0
    cnt = 0
    while cnt < 200:
        cnt += 1
        t += 0.1
        yield t,np.sin(2 * np.pi * t) * np.exp(-t / 10.)
 
 
def init():
    ax.set_ylim(-1.1,1.1)
    ax.set_xlim(0,10)
    line.set_data([],[])
    return line,
 
 
def update(datag):
    # update the data，默认接受后面的yield
    t,y = datag
    xdata.append(t)
    ydata.append(y)
    line.set_data(xdata,ydata)
 
    if max(xdata) > 10:
        ax.set_xlim(max(xdata) - 10,max(xdata))
    return line,
 
 
fig,ax = plt.subplots()
line, = ax.plot([],[],lw=2)
ax.grid()
xdata,ydata = [],[]
 
# 参数：{画布，绘制图像函数，更新数据函数，时间间隔，重复标识，初始化函数}
ani = animation.FuncAnimation(fig,update,data_gen,interval=10,repeat=False,init_func=init)
plt.show()

#%matplotlib qt