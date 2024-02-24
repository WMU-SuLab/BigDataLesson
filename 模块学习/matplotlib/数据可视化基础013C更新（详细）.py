# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:58:45 2018

@author: 高治国
"""
#升级之后使用以下命令可以更好的观察图像
#%matplotlib qt

#多图显示
import matplotlib.pyplot as plt
import numpy as np

plt.figure()

# 将整个figure分成两行两列
plt.subplot(2, 2, 1)
# 第一个参数表示X的范围，第二个是y的范围
plt.plot([0, 1], [0, 1])

plt.subplot(222)
plt.plot([0, 1], [0, 2])

plt.subplot(223)
plt.plot([0, 1], [0, 3])

plt.subplot(224)
plt.plot([0, 1], [0, 4])

plt.show()

#分割显示
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

plt.figure()
# 第一个元素表示将总的面板进行划分，划分为3行3列，
# 第二个元素表示该面板从0行0列开始，列的跨度（colspan）为3列，行的跨度（rowspan）为1
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
# 第一个元素的表示X的范围为[1,2]，第二个元素表示Y的范围为[1,2]
ax1.plot([1, 2], [1, 2])
ax1.set_title(r'$ax1\_title$')
# 第一个元素表示将总的面板进行划分，划分为3行3列，
# 第二个元素表示该面板从1行0列开始，列的跨度（colspan）为2列，行的跨度（rowspan）取默认值1
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax2.plot([1, 2], [1, 2])
ax2.set_title(r'$ax2\_title$')
# 第一个元素表示将总的面板进行划分，划分为3行3列，
# 第二个元素表示该面板从1行2列开始，行的跨度（rowspan）为2列，列的跨度（colspan）取默认值1
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax3.plot([1, 2], [1, 2])
ax3.set_title(r'$ax3\_title$')
# 第一个元素表示将总的面板进行划分，划分为3行3列，
# 第二个元素表示该面板从2行0列开始,行的跨度（rowspan）为2列，列的跨度（colspan）取默认值1
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.plot([1, 2], [1, 2])
ax4.set_title(r'$ax4\_title$')
# 第一个元素表示将总的面板进行划分，划分为3行3列，
# 第二个元素表示该面板从2行1列开始,行的跨度（rowspan）为2列，列的跨度（colspan）取默认值1
ax5 = plt.subplot2grid((3, 3), (2, 1))
ax5.plot([1, 2], [1, 2])
ax5.set_title(r'$ax5\_title$')

plt.tight_layout()
plt.show()

#图中图
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 6))
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

# 大图
left, bottom, width, weight = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, weight])
ax1.plot(x, y, 'r')
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$y$')
ax1.set_title(r'$××Interesting××$')

# 左上小图
left, bottom, width, weight = 0.2, 0.6, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, weight])
ax2.plot(y, x, 'b')
ax2.set_xlabel(r'$x$')
ax2.set_ylabel(r'$y$')
ax2.set_title(r'$title\ inside\ 1$')

# 右下小图
plt.axes([0.6, 0.2, 0.25, 0.25])
# 将y的数据逆序输出[::1]
plt.plot(y[::-1],x, 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'$title\ inside\ 2$')

plt.show()

#主次坐标
import matplotlib.pyplot as plt
import numpy as np

# 从[0, 10]以0.1为间隔，形成一个列表
x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 * y1


fig, ax1 = plt.subplots()
# 镜像（上下左右颠倒）
ax2 = ax1.twinx()
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b--')

# 为轴进行命名
ax1.set_xlabel(r'$X\ data$', fontsize=16)
ax1.set_ylabel(r'$Y1$', color='g', fontsize=16)
ax2.set_ylabel(r'$Y2$', color='b', fontsize=16)

plt.show()

#