# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 13:24:09 2018

@author: 高治国
"""

numpy.ndarray.tolist()

#注意事项

数学上定义的矩阵乘法 np.dot(a, b)。如果形状不匹配会报错；但是允许允许a和b都是向量，返回两个向量的内积。只要有一个参数不是向量，就应用矩阵乘法。

读取数组元素：如a[0],a[0,0]

数组变形：如b=a.reshape(2,3,4)将得到原数组变为2*3*4的三维数组后的数组；或是a.shape=(2,3,4)或a.resize(2,3,4)直接改变数组a的形状

数组组合：水平组合hstack((a,b))或concatenate（（a,b）,axis=1）;垂直组合vstack((a,b))或concatenate（（a,b）,axis=0）;深度组合dstack((a,b))

数组分割（与数组组合相反）：分别有hsplit,vsplit,dsplit,split(split与concatenate相对应)

将np数组变为py列表：a.tolist()

数组排序（小到大）：列排列np.msort(a)，行排列np.sort(a)，np.argsort(a)排序后返回下标

复数排序：np.sort_complex(a)按先实部后虚部排序

数组的插入：np.searchsorted(a,b)将b插入原有序数组a，并返回插入元素的索引值

类型转换：如a.astype(int)，np的数据类型比py丰富，且每种类型都有转换方法

条件查找，返回满足条件的数组元素的索引值：np.where(条件)

条件查找，返回下标：np.argwhere(条件)

条件查找，返回满足条件的数组元素：np.extract([条件],a)

根据b中元素作为索引，查找a中对应元素：np.take(a,b)一维

数组中最小最大元素的索引：np.argmin(a)，np.argmax(a)

多个数组的对应位置上元素大小的比较：np.maximum(a,b,c,…..)返回每个索引位置上的最大值，np.minimum(…….)相反

将a中元素都置为b：a.fill(b)

每个数组元素的指数：np.exp(a)

生成等差行向量：如np.linspace(1,6,10)则得到1到6之间的均匀分布，总共返回10个数

求余：np.mod(a,n)相当于a%n，np.fmod(a,n)仍为求余且余数的正负由a决定

计算平均值：np.mean(a)

计算最大值：amax(a, axis=None, out=None, keepdims=False) 。Return the maximum of an array or maximum along an axis.

计算加权平均值：np.average(a,b),其中b是权重

计算数组的极差：np.pth(a)=max(a)-min(a)

计算方差（总体方差）：np.var(a)

标准差：np.std(a)

算术平方根，a为浮点数类型：np.sqrt(a)

对数：np.log(a)

修剪数组，将数组中小于x的数均换为x，大于y的数均换为y：a.clip(x,y)

所有数组元素乘积：a.prod()

数组元素的累积乘积：a.cumprod()

数组元素的符号：np.sign(a)，返回数组中各元素的正负符号，用1和-1表示

数组元素分类：np.piecewise(a,[条件]，[返回值])，分段给定取值，根据判断条件给元素分类，并返回设定的返回值。

判断两数组是否相等： np.array_equal(a,b)

判断数组元素是否为实数： np.isreal(a)

去除数组中首尾为0的元素：np.trim_zeros(a)

对浮点数取整，但不改变浮点数类型：np.rint(a)
