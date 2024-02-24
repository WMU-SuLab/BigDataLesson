# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:13:32 2018

@author: 高治国
"""
#散点图
import matplotlib.pyplot as plt
import numpy as np

n = 128
#随机数
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
scatter(X,Y,color = 'r')

n = 64
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
scatter(X,Y,color = 'b')

show()

#条形图
import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)

plt.figure(figsize=(12, 8))
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X,Y1):
    # ha: horizontal alignment水平方向
    # va: vertical alignment垂直方向
    plt.text(x, y+0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X,-Y2):
    # ha: horizontal alignment水平方向
    # va: vertical alignment垂直方向
    plt.text(x, y-0.05, '%.2f' % y, ha='center', va='top')

# 定义范围和标签
plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()


#等高线
import matplotlib.pyplot as plt
import numpy as np

def get_height(x, y):
    # the height function
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

plt.figure(figsize=(14, 8))

# use plt.contourf to filling contours
# X, Y and value for (X, Y) point

# 横坐标、纵坐标、高度、 、透明度、cmap是颜色对应表
# 等高线的填充颜色
plt.contourf(X, Y, get_height(X, Y), 16, alpah=0.1, cmap=plt.cm.hot)  

# use plt.contour to add contour lines
# 这里是等高线的线
C = plt.contour(X, Y, get_height(X, Y), 16, color='black', linewidth=.5)

# adding label
plt.clabel(C, inline=True, fontsize=16)

plt.xticks(())
plt.yticks(())
plt.show()


#3D图
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 8))
ax = Axes3D(fig)

# 生成X，Y
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X,Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)

# height value
Z = np.sin(R)

# 绘图
# rstride（row）和cstride(column)表示的是行列的跨度
ax.plot_surface(X, Y, Z, 
                rstride=1,  # 行的跨度
                cstride=1,  # 列的跨度
                cmap=plt.get_cmap('rainbow')  # 颜色映射样式设置
               )

# offset 表示距离zdir的轴距离
ax.contourf(X, Y, Z, zdir='z', offest=-2, cmap='rainbow')
ax.set_zlim(-2, 2)

plt.show()
