# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:43:20 2018

@author: 高治国
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
 
# 1.First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0,2),ylim=(-2,2))
line, = ax.plot([],[],lw=2)
 
 
# 2.initialization function: plot the background of each frame
def init():
    line.set_data([],[])
    return line,
 
 
# 3.animation function.  This is called sequentially
# note: i is framenumber
def update(i):
    x = np.linspace(0,2,1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))  # 调整x相当于向右平移图像
    line.set_data(x,y)
    return line,
 
 
# call the animator.  blit=True means only re-draw the parts that have changed.
# 画布， 使用帧数做参数的绘制函数， init生成器.。
anim = animation.FuncAnimation(fig,update,init_func=init,frames=200,interval=20,blit=False)
# frames=200   帧数
# interval=20  间隔
 
# anim.save('anim3.mp4', fps=30, extra_args=['-vcodec', 'libx264'])      # 保存为mp4
# anim.save('anim3.gif', writer='imagemagick')                           # 保存为gif
 
plt.show()

#%matplotlib qt