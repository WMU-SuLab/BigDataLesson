# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:56:09 2018

@author: 高治国
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
 
fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(np.zeros(9),'bo')  # 由于没有使用init_fun，所以初始帧有数据，且尺寸与后续帧一致才行
ax.set_xlim(0,10)
ax.set_ylim(0,10)
ax.set_xticks(np.linspace(0,10,11))
ax.set_yticks(np.linspace(0,10,11))
ax.grid(True)
 
# update的参数是调用函数data_gen
def update(data):
    line.set_xdata(np.linspace(1,9,9))
    line.set_ydata(data)
    return line,
 
def data_gen():
    x = [9,8,3,1,2,4,6,5,7]
    for i in range(len(x)-1):
        for j in range(len(x)-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
            yield(x)
 
# {画布，绘制函数(数据函数yield)，数据函数，帧间隔(毫秒),重复标识}
ani = animation.FuncAnimation(fig,update,data_gen,interval=1000,repeat=False)
plt.show()

#%matplotlib qt