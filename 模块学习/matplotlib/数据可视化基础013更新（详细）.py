# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:21:57 2018

@author: 高治国
"""

#简单线图
import matplotlib.pyplot as plt
import numpy as np

# 从[-1,1]中等距去50个数作为x的取值
x = np.linspace(-1, 1, 50)
y = 2**x + 1
# 第一个是横坐标的值，第二个是纵坐标的值
plt.plot(x, y)
# 必要方法，用于将设置好的figure对象显示出来
plt.show()

#多个图像
import matplotlib.pyplot as plt
import numpy as np

# 多个figure
x = np.linspace(-1, 1, 50)
y1 = 2*x + 1
y2 = 2**x + 1

# 使用figure()函数重新申请一个figure对象
# 注意，每次调用figure的时候都会重新申请一个figure对象
plt.figure()
# 第一个是横坐标的值，第二个是纵坐标的值
plt.plot(x, y1)

# 第一个参数表示的是编号，第二个表示的是图表的长宽
plt.figure(num = 3, figsize=(8, 5))

# 设置轴线的lable（标签）
plt.xlabel("I am x")
plt.ylabel("I am y") 

# 当我们需要在画板中绘制两条线的时候，可以使用下面的方法：
plt.plot(x, y2)
plt.plot(x, y1,
         color='red',   # 线颜色
         linewidth=1.0,  # 线宽 
         linestyle='--'  # 线样式
        )


#复杂一些的图
import matplotlib.pyplot as plt
import numpy as np

# 从[-1,1]中等距去50个数作为x的取值
x = np.linspace(-1, 1, 50)
y1 = 2*x + 1
y2 = 2**x + 1
# num表示的是编号，figsize表示的是图表的长宽
plt.figure(num = 3, figsize=(8, 5))  
plt.plot(x, y2)
# 设置线条的样式
plt.plot(x, y1, 
         color='red',  # 线条的颜色
         linewidth=1.0,  # 线条的粗细
         linestyle='--'  # 线条的样式
        )

# 设置取值参数范围
plt.xlim((-1, 2))  # x参数范围
plt.ylim((1, 3))  # y参数范围

# 设置点的位置
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
# 为点的位置设置对应的文字。
# 第一个参数是点的位置，第二个参数是点的文字提示。
plt.yticks([-2, -1.8, -1, 1.22, 3],
          [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$readly\ good$'])

# gca = 'get current axis'
ax = plt.gca()
# 将右边和上边的边框（脊）的颜色去掉
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 绑定x轴和y轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 定义x轴和y轴的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.show()

#曲线说明
import matplotlib.pyplot as plt
import numpy as np

# 从[-1,1]中等距去50个数作为x的取值
x = np.linspace(-1, 1, 50)
y1 = 2*x + 1
y2 = 2**x + 1

# 第一个参数表示的是编号，第二个表示的是图表的长宽
plt.figure(num = 3, figsize=(8, 5))  
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# 设置取值参数
plt.xlim((-1, 2))
plt.ylim((1, 3))

# 设置lable
plt.xlabel("I am x")
plt.ylabel("I am y")

# 设置点的位置
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22,3],
          [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$readly\ good$'])


l1, = plt.plot(x, y2, 
               label='aaa'
              )
l2, = plt.plot(x, y1, 
               color='red',  # 线条颜色
               linewidth = 1.0,  # 线条宽度
               linestyle='-.',  # 线条样式
               label='bbb'  #标签
              )

# 使用ｌｅｇｅｎｄ绘制多条曲线
plt.legend(handles=[l1, l2], 
           labels = ['aaa', 'bbb'], 
           loc = 'best'
          )

#点的注释

import matplotlib.pyplot as plt
import numpy as np

# 从[-1,1]中等距去50个数作为x的取值
x = np.linspace(-1, 1, 50)
y1 = 2*x + 1
y2 = 2**x + 1

plt.figure(figsize=(12, 8))  # 第一个参数表示的是编号，第二个表示的是图表的长宽
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# gca = 'get current axis'
ax = plt.gca()
# 将右边和上边的边框（脊）的颜色去掉
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 绑定x轴和y轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 定义x轴和y轴的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 显示交叉点
x0 = 1
y0 = 2*x0 + 1
# s表示点的大小，默认rcParams['lines.markersize']**2
plt.scatter(x0, y0, s = 66, color = 'b')
# 定义线的范围，X的范围是定值，y的范围是从y0到0的位置
# lw的意思是linewidth,线宽
plt.plot([x0, x0], [y0, 0], 'k-.', lw= 2.5)

# 设置关键位置的提示信息
plt.annotate(r'$2x+1=%s$' % 
             y0, 
             xy=(x0, y0), 
             xycoords='data',

             xytext=(+30, -30),
             textcoords='offset points',
             fontsize=16,  # 这里设置的是字体的大小
             # 这里设置的是箭头和箭头的弧度
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2')
            )

# 在figure中显示文字信息
# 可以使用\来输出特殊的字符\mu\ \sigma\ \alpha
plt.text(0, 3, 
         r'$This\ is\ a\ good\ idea.\ \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size':16,'color':'r'})


#能见度
import matplotlib.pyplot as plt
import numpy as np

# 从[-1,1]中等距去50个数作为x的取值
x = np.linspace(-1, 1, 50)
y = 2*x - 1

plt.figure(figsize=(12, 8))  # 第一个参数表示的是编号，第二个表示的是图表的长宽
# alpha是设置透明度的
plt.plot(x, y, color='r', linewidth=10.0, alpha=0.5)

# gca = 'get current axis'
ax = plt.gca()
# 将右边和上边的边框（脊）的颜色去掉
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 绑定x轴和y轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 定义x轴和y轴的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 可以使用tick设置透明度
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='y', edgecolor='None', alpha=0.7))

plt.show()


#

#

#

#

#

#

