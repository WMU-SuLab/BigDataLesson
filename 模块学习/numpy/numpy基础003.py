# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 08:53:51 2018

@author: 高治国
"""

import numpy

#第1节创建数组
#使用列表生成一维数组
dataL = [1,2,3,4,5,6]
#使用列表生成二维数组
dataL = [[1,2],[3,4],[5,6]]
#三维
dataL =[[[1,2],[3,4],[5,6]],[[1,2],[3,4],[5,6]]]
#重点：体会：块（关系、二维表）、行（元祖、记录）、列（字段、属性）的语义
#对数据的理解的重要性远远超过语法
x = numpy.array(dataL)
#numpy.array()生成一个ndarray，x就是ndarray的一个实例
x.ndim #数组的维度
x.shape #数组各个维度的长度。重点：shape是一个元组
x.dtype #数组元素的类型
x.dtype.name
x.size #元素个数
x.itemsize#每个元素字节大小，单位:B
x.data#缓冲区
#使用zero/ones/empty创建数组:根据shape来创建'
x = numpy.zeros(6) #创建一维长度为6的，元素都是0一维数组
x = numpy.zeros((2,3)) #创建一维长度为2，二维长度为3的二维0数组
x = numpy.ones((2,3)) #创建一维长度为2，二维长度为3的二维1数组
x = numpy.empty((3,3)) #创建一维长度为2，二维长度为3,未初始化的二维数组
#函数empty创建一个内容随机并且依赖与内存状态的数组。默认创建的数组类型(dtype)都是float64。

#使用arrange生成连续元素
x=numpy.arange(6) # [0,1,2,3,4,5,] 开区间
x=numpy.arange(0,6,2)  # [0, 2，4]

#numpy数组改变维度
x = arange(15).reshape(3, 5)

#其他一些常用参数和用法
x = np.array([1,  2,  3], dtype = complex)  
x = array( [ (1.5,2,3), (4,5,6) ] )
x=ones( (2,3,4), dtype=int16 ) 
#特殊需求：将字符转成数值 容易出错
x = numpy.array(['1','2','3'],dtype = numpy.string_)
y = x.astype(numpy.int64)
#等价、约等于
x = numpy.array(['1','2','3'],dtype = int64)

#其它函数array, zeros, zeros_like, ones, ones_like, empty, empty_like, arange, linspace, rand, randn, fromfunction, fromfile参考：NumPy示例

#第2节索引和切片   合并和拆解

#访问，就是切片
import numpy as np
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],dtype=int)
x[0,1]  #1行 第二个单元元素
x[:,1]  #所有行 第二个单元元素
x[1,:]  #2行 所有单元元素 
x[1,1:]  #2行 第2个单元开始以后所有元素
x[1,:2]  #2行 第1个单元开始到索引为2以前的所有元素

#切片还可以包括省略号（...），来使选择元组的长度与数组的维度相同。 
#如果在行位置使用省略号，它将返回包含行中元素的ndarray。
import numpy as np
x = np.array([[1,2,3],[3,4,5],[4,5,6]])  
# 这会返回第二列元素的数组：  
x[...,1]  
# 现在我们从第二行切片所有元素：  
x[1,...]  
# 现在我们从第二列向后切片所有元素：
x[...,1:]


#练习一下
x=numpy.array([[1,2],[3,4],[5,6]])
x[0]#[1,2]
x[0][1]#2,普通python数组的索引
x[0,1]#同x[0][1]，ndarray数组的索引
x=numpy.array([[[1,2],[3,4]],[[5,6],[7,8]]])
x[0]#[[12],[34]]
x[0,0]
y=x[0].copy()#生成一个副本
z=x[0]#未生成一个副本
y#[[12],[34]]
y[0,0]#1
#注意数组本身和副本的区别
y[0,0]=0
z[0,0]=-1
y#[[02],[34]]
x[0]#[[-12],[34]]
z#[[-12],[34]]

#ndarray的切片 体会块、列、行
x=numpy.array([1,2,3,4,5])
x[1:3]#[2,3]右边开区间
x[:3]#[1,2,3]左边默认为0
x[1:]#[2,3,4,5]右边默认为元素个数
x[0:4:2]#[1,3]下标递增2
x=numpy.array([[1,2],[3,4],[5,6]])
x[:2]#[[12],[34]]
x[:2,:1]#[[1],[3]]
x[:2,:1]=0#用标量赋值
x#[[0,2],[0,4],[5,6]]
x[:2,:1]=[[8],[6]]#用数组赋值
x#[[8,2],[6,4],[5,6]]

#2.1ndarray数组的布尔索引和花式索引
#arr[condition]，condition为一个条件/多个条件组成的布尔数组。
x = numpy.array([3,2,3,1,3,0])
#对比
x = numpy.array([[3,2,3],[1,3,0]])
# 布尔型数组的长度必须跟被索引的轴长度一致
y = numpy.array([True,False,True,False,True,False]) 
#对比
y = numpy.array([[True,False,True],[False,True,False]])
x[y]#[3,3,3]
x[y==False]#[2,1,0]
x>=3#[TrueFalseTrueFalseTrueFalse]
x[~(x>=3)]#[2,1,0]
(x==2)|(x==1)#[FalseTrueFalseTrueFalseFalse]
x[(x==2)|(x==1)]#[21]
x[(x==2)|(x==1)]=0
x#[303030]

#花式索引 重点区分索引和切片的区别
x=numpy.array([1,2,3,4,5,6])
x[[0,1,2]]#[123]
x[[-1,-2,-3]]#[6,5,4]

x=numpy.array([[1,2],[3,4],[5,6]])
x[[0,1]]#[[1,2],[3,4]]
x[[0,1],[0,1]]#[1,4]打印x[0][0]和x[1][1]
#先索引一次再索引一次
x[[0,1]][:,[0,1]]#打印01行的01列[[1,2],[3,4]]

x = np.array([[1,  2],  [3,  4],  [5,  6]]) 
y = x[[0,1,2],  [0,1,0]]  

#使用numpy.ix_()函数增强可读性
x[numpy.ix_([0,1],[0,1])]#同上打印01行的01列[[1,2],[3,4]]
x[[0,1],[0,1]]=[0,0]
x#[[0,2],[3,0],[5,6]]

#练习一下 注意一下数据语义上的含义
import numpy as np 
x=np.arange(20).reshape(4,5)
y=x[[[0,0],[1,1]],[[0,1],[0,1]]]
y=x[[[0,0],[1,1]],[[0,2],[0,2]]]
y=x[[[0,0],[2,2]],[[0,2],[0,2]]]
# 合并，注意多个方向
import numpy as np
a = np.array([1, 1, 1])
b = np.array([2, 2, 2])
# 合并array, 竖直方向
c = np.vstack((a, b))
# 合并array, 水平方向
d = np.hstack((a, b))

# 添加维度
# 列方向上添加维度
a = np.array([1, 1, 1])
b = a[:, np.newaxis]
# 行方向上添加维度
c = a[np.newaxis, :]

# a, b列方向添加维度
a = np.array([1, 1, 1])
b = np.array([2, 2, 2])
a = a[:, np.newaxis]
b = b[:, np.newaxis]
# 合并多个array并指定合并的维度, 列方向上合并
c = np.concatenate((a, b, b, a), axis = 0)
# 合并多个array并指定合并的维度, 行方向上合并
d = np.concatenate((a, b, b, a), axis = 1)

#拆分
#默认情况下，Numpy数组是按行优先顺序创建。
#在空间方面，这就意味着，对于一个二维数字，每行中的数据项是存放在内在中相邻的位置上的。
#另一种顺序是列优先。由于历史原因，行优先和列优先又分别被称为C和Fortran顺序。
#在Numpy中，可以通过关键字参数order='C' 和order='F' 来实现行优先和列优先。
x=np.arange(15).reshape(3,-1)
x.ravel('F') #按照列优先，扁平化。
x.ravel()
x.reshape((5,3),order='F') # Fortran 顺序
x.reshape((5,3),order='C')

a=np.arange(9).reshape(3,3)
b=a*2
#行
np.hstack((a,b))
np.concatenate((a,b),axis=1)
#列
np.vstack((a,b))
np.concatenate((a,b),axis=0)
#深度
np.dstack((a,b))

#切割
a = np.arange(12).reshape(3, 4)
# 纵向分割, 分成两部分, 按列分割  特别注意返回的类型
np.split(a, 2, axis = 1)
np.array_split(a, 3, axis = 1)  #不均分
# 横向分割, 分成三部分, 按行分割
np.split(a, 3, axis = 0)

# 垂直方向分割
np.vsplit(a, 3)
# 水平方向分割
np.hsplit(a, 2)

#如何遍历数组
a = np.arange(9).reshape(3,3) 
for row in a:
  print (row) 
#对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
for element in a.flat:
  print (element)

#这一部分相当于numpy提供的输入输出，学习过panda可以略过。
#数组序列化和反序列化  注意：输入输出我们一般使用panda了，这里了解即可
#序列化是将对象状态转换为可保持或传输的形式的过程。序列化的补集是反序列化，后者将流转换为对象。这两个过程一起保证数据易于存储和传输。
#预定义数据栏位名称和类型  
table = np.loadtxt('example.txt',dtype='names': ('ID', 'Result', 'Type'),\  
    'formats': ('S4', 'f4', 'i2'))  
np.savetxt('somenewfile.txt')#序列化  
#二进制文件加载，保存  
data = np.empty((1000, 1000))  
np.save('test.npy', data)  
np.savez('test.npz', data)#采用压缩  
newdata = np.load('test.npy')   

#判断数组是否共享内存，也是用来直接判断数据是复制的还是镜像的
#如果能理解镜像和复制的区别可以跳过这部分
#方法一：
a = np.arange(50)
b = a.reshape((5, 10))
b.base is a
 #方法二：
np.may_share_memory(a, b)
#方法三：
b.flags['OWNDATA'] #False -- apparently this is a view
e = np.ravel(b[:, 2])
e.flags['OWNDATA']  #True -- Apparently this is a new numpy object.



#第3节：数组转置 重要
#数组的转置/轴对换只会返回源数据的一个视图，不会对源数据进行修改。
import numpy as np 

#numpy.transpose这个函数翻转给定数组的维度。
#如果可能的话它会返回一个视图。函数接受下列参数：numpy.transpose(arr, axes)
#其中：arr：要转置的数组
#axes：整数的列表，对应维度
x = np.arange(15).reshape(3,5)
np.transpose(x)
x.transpose((1,0))
x.T

#转置 更重要 更难理解
x = np.arange(12).reshape((2,3,2))
#考虑三维在二维上的映射
#对于高维数组，transpose需要得到一个由轴编号组成的元组才能对这些轴进行转置
#原样不变
#等价方法
# 轴交换 swapaxes (axes：轴)，参数:一对轴编号
#numpy.swapaxes该函数交换数组的两个轴。
#这个函数接受下列参数：numpy.swapaxes(arr, axis1, axis2)
#arr：要交换其轴的输入数组
#axis1：对应第一个轴的整数
#axis2：对应第二个轴的整数

x.transpose((0,1,2))
#重点：0代表块、1代表列、2带表行
x.transpose((0,2,1))
x.swapaxes(1,2)

#看效果代表了基础的维度上转置 想象一个立方体 ！！
#比如原来位置（0,1,0）上的元素为4，现在把它放到了（1,0,0）这个位置
x.transpose((1,0,2))# m[y][x][z] = k[x][y][z]
x.swapaxes(0,1)
#另外，转置（2，0，1）可以看成，先转置（0，2，1）再转置（1，0，2）
#低纬先转比较容易理解
#转置（2，1，0）可以看成，先转置（1，0，2），然后转置（0，2，1），最后转置（1，0，2）
#转置（1，2，0）可以看成，先转置（1，0，2），在转置（0，2，1）
#数组的转置/轴对换只会返回源数据的一个视图，不会对源数据进行修改。

#numpy.rollaxis该函数向后滚动特定的轴，直到一个特定位置。
#这个函数接受三个参数：numpy.rollaxis(arr, axis, start)
#其中：
#arr：输入数组
#axis：要向后滚动的轴，其它轴的相对位置不会改变
#start：默认为零，表示完整的滚动。会滚动到特定位置。
# 创建了三维的 ndarray
import numpy as np
a = np.arange(8).reshape(2,2,2)
# 将轴 2 滚动到轴 0(宽度到深度)
np.rollaxis(a,2)  
# 将轴 2 滚动到轴 1：(宽度到高度)
np.rollaxis(a,2,1)


#第4节添加删除元素
#numpy.resize此函数返回指定大小的新数组。 
#如果新大小大于原始大小，则包含原始数组中的元素的重复副本。 
#该函数接受以下参数。numpy.resize(arr, shape)
#arr：要修改大小的输入数组
#shape：返回数组的新形状例子
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
a.shape
np.resize(a, (3,2))
b.shape
# 要注意 a 的第一行在 b 中重复出现，因为尺寸变大了
np.resize(a,(3,3))

#numpy.append此函数在输入数组的末尾添加值。 附加操作不是原地的，而是分配新的数组。 
#此外，输入数组的维度必须匹配否则将生成ValueError。
#numpy.append(arr, values, axis)
#arr：输入数组
#values：要向arr添加的值，比如和arr形状相同(除了要添加的轴)
#axis：沿着它完成操作的轴。如果没有提供，两个参数都会被展开。
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
np.append(a, [7,8,9])
#沿轴 0 添加元素：
np.append(a, [[7,8,9]],axis = 0)
#沿轴 1 添加元素：
np.append(a, [[5,5,5],[7,8,9]],axis = 1)

#numpy.insert此函数在给定索引之前，沿给定轴在输入数组中插入值。 
#如果值的类型转换为要插入，则它与输入数组不同。 插入没有原地的，函数会返回一个新数组。 
#此外，如果未提供轴，则输入数组会被展开。
#numpy.insert(arr, obj, values, axis)
#arr：输入数组
#obj：在其之前插入值的索引
#values：要插入的值
#axis：沿着它插入的轴，如果未提供，则输入数组会被展开
import numpy as np
a = np.array([[1,2],[3,4],[5,6]])
np.insert(a,3,[11,12])
#'沿轴 0 广播：'
np.insert(a,1,[11],axis = 0)
#'沿轴 1 广播：'
np.insert(a,1,11,axis = 1)


#删除
#numpy.delete此函数返回从输入数组中删除指定子数组的新数组。 
#与insert()函数的情况一样，如果未提供轴参数，则输入数组将展开。 
#该函数接受以下参数：Numpy.delete(arr, obj, axis)
#其中：arr：输入数组obj：可以被切片，整数或者整数数组，表明要从输入数组删除的子数组
#axis：沿着它删除给定子数组的轴，如果未提供，则输入数组会被展开
import numpy as np
a = np.arange(12).reshape(3,4)
np.delete(a,5)
np.delete(a,1,axis = 1)
np.delete(a,1,axis = 0)

a = np.array([1,2,3,4,5,6,7,8,9,10])
np.delete(a, np.s_[::2])




#第5节基本运算
a = array( [20,30,40,50] )
b = arange( 4 )
c = a-b
b**2
10*sin(a)
array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
a<35
# 计算矩阵的内积 xTx
numpy.dot(m,m.T) # numpy.dot点乘
#广播
#如果两个数组的维数不相同，则元素到元素的操作是不可能的。 
#然而，在 NumPy 中仍然可以对形状不相似的数组进行操作，因为它拥有广播功能。 
#较小的数组会广播到较大数组的大小，以便使它们的形状可兼容。
import numpy as np 
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0])  
a+b

#乘法和矩阵乘法
A = array( [[1,1],[0,1]] )
B = array( [[2,0],[3,4]] )
A*B                         # elementwise product
dot(A,B)                    # matrix product

#有些操作符像+=和*=被用来更改已存在数组而不创建一个新的数组。
#特别注意他们改动了内存中的数据而不是镜像（视图）
a = ones((2,3), dtype=int)
b = random.random((2,3))
a *= 3
b += a
a += b   

#当运算的是不同类型的数组时，结果数组类型更普遍和精确(这种行为叫做upcast)
a = ones(3, dtype=int32)
b = linspace(0,pi,3)
b.dtype.name
c = a+b
c.dtype.name
d = exp(c*1j)
d.dtype.name

#第5节 基本函数
#numpy的算数运算符都是对python内置运算符的封装。
x = np.arange(4)
x+2
np.add(x,2)#加法
x-2
np.subtract(x,2)#减法
x*2
np.multiply(x,2)#乘法
x/2
np.divide(x,2)#除法
x**2
np.power(x,2)#乘方
x//2
np.floor_divide(x,2)#地板除法
x%2
np.mod(x,2)#取余
np.abs(x)#取绝对值
x=np.linspace(0,np.pi,3)#180°均分成3份
np.sin(x)#正弦函数
np.cos(x)#余弦函数
np.tan(x)#正切函数
#指数及对数运算
x=np.array([1,2,3])
np.exp(x)
np.power(3,x)
x=np.array([1,8,64,100])
np.log(x) #自然对数ln(x)
np.log2(x)
np.log10(x)
#其他常用函数
np.abs(a) 
np.fabs(a) # 取各元素的绝对值 
np.sqrt(a) # 计算各元素的平方根 
np.square(a)# 计算各元素的平方 
np.log(a) 
np.log10(a) 
np.log2(a) # 计算各元素的自然对数、10、2为底的对数 
np.ceil(a) 
np.floor(a) # 计算各元素的ceiling 值， floor值（ceiling向上取整，floor向下取整） 
np.rint(a) # 各元素 四舍五入 
np.modf(a) # 将数组各元素的小数和整数部分以两个独立数组形式返回 
np.exp(a) # 计算各元素的指数值 
np.sign(a) # 计算各元素的符号值 1（+），0，-1（-） 
np.maximum(a, b) 
np.fmax() # 比较（或者计算）元素级的最大值 
np.minimum(a, b) 
np.fmin() # 取最小值 
np.mod(a, b) # 元素级的模运算 
np.copysign(a, b) # 将b中各元素的符号赋值给数组a的对应元素
#注意以下比较特殊的通用函数
a = np.arange(9)
np.add.reduce(a)
np.add.accumulate(a)
np.add.reduceat(a, [0, 5, 2, 7])
#第一步用到索引值列表中的0和5，实际上就是对数组中索引值在0到5之间的元素进行reduce操作。 
#第二步用到索引值5和2。由于2比5小，所以直接返回索引值为5的元素。 
#第三步用到索引值2和7。这一步是对索引值在2到7之间的数组元素进行reduce操作。 
#第四步用到索引值7。这一步是对索引值从7开始直到数组末端的元素进行reduce操作。 
#暂时不能掌握没关系，先跳过去，很多函数非常高深，用途的面也小
np.add.outer(np.arange(3), a)
#outer方法返回一个数组，它的秩（rank）等于两个输入数组的秩的和。它会作用于两个输入数组之间存在的所有元素对。

#全数组运算
a.sum()
a.min()
a.max()
#数组运算 加减乘除
import numpy as np 
a = np.arange(9, dtype = np.float_).reshape(3,3)  
b = np.array([10,10,10])  
np.add(a,b)  
np.subtract(a,b)  
np.multiply(a,b)  
np.divide(a,b)

#此函数返回参数逐元素的倒数
#由于 Python 处理整数除法的方式，对于绝对值大于 1 的整数元素，结果始终为 0， 对于整数 0，则发出溢出警告。 
a = np.array([0.25,  1.33,  1,  1,  100])  
np.reciprocal(a)  
b = np.array([100], dtype =  int)  
np.reciprocal(b)

#此函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂。
import numpy as np 
a = np.array([10,100,1000])
np.power(a,2)  
b = np.array([1,2,3])  
np.power(a,b)

#此函数返回输入数组中相应元素的除法余数。 
#函数numpy.remainder()也产生相同的结果。
import numpy as np 
a = np.array([10,20,30]) 
b = np.array([3,5,7])  
np.mod(a,b)  
np.remainder(a,b)

#numpy.real() 返回复数类型参数的实部。
#numpy.imag() 返回复数类型参数的虚部。
#numpy.conj() 返回通过改变虚部的符号而获得的共轭复数。
#numpy.angle() 返回复数参数的角度。 
#函数的参数是degree。 如果为true，返回的角度以角度制来表示，否则为以弧度制来表示。

#三角函数
#NumPy 拥有标准的三角函数，它为弧度制单位的给定角度返回三角函数比值。示例import numpy as np
a = np.array([0,30,45,60,90])  
# 通过乘 pi/180 转化为弧度  
np.sin(a*np.pi/180)  
np.cos(a*np.pi/180)  
np.tan(a*np.pi/180)
#arcsin，arccos，和arctan函数返回给定角度的sin，cos和tan的反三角函数。 
#这些函数的结果可以通过numpy.degrees()函数通过将弧度制转换为角度制来验证。
a = np.array([0,30,45,60,90])  
sin = np.sin(a*np.pi/180)  
inv = np.arcsin(sin)  
np.degrees(inv)  
cos = np.cos(a*np.pi/180)  
inv = np.arccos(cos)  
np.degrees(inv)  
tan = np.tan(a*np.pi/180)  
inv = np.arctan(tan)  
np.degrees(inv)
#四舍五入
import numpy as np
a = np.array([1.0,5.55,  123,  0.567,  25.532])  
np.around(a)  
np.around(a, decimals =  1)  
np.around(a, decimals =  -1)

#numpy.floor()此函数返回不大于输入参数的最大整数。 
#即标量x 的下限是最大的整数i ，使得i <= x。 
a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])  
np.floor(a)
#numpy.ceil()ceil()函数返回输入值的上限，
#即，标量x的上限是最小的整数i ，使得i> = x。
np.ceil(a)

#numpy中的随机数模块
rand() 　　#产生[0,1]的浮点随机数,括号里面的参数可以指定产生数组的形状
randn()　　#产生标准正太分布随机数，参数含义与random相同
randint()　　#产生指定范围的随机数，最后一个参数是元祖，他确定数组的形状
import numpy as np
from numpy import random as nr
#只显示小数点后两位
np.set_printoptions(precision = 2)
r1 = nr.rand(3,4)
r2 = nr.randn(5,4)
r3 = nr.randint(0,10,size = (4,3))

#normal(）　　正太分布
#uniform()　　均匀分布
#poisson()　　泊松分布
import numpy as np
from numpy import random as nr
 
#只显示小数点后两位
np.set_printoptions(precision = 2)
 
#第一个参数是均值，第二个参数是标准差
r1 = nr.normal(100,10,size = (3,4))
 
#前两个参数分别是区间的初始值和终值
r2 = nr.uniform(0,10,size = (3,4))
 
#第一个参数为指定的lanbda系数
r3 = nr.poisson(2.0,size = (3,4))

#乱序和随机抽取
#permutation()随机生成一个乱序数组，当参数是n时，返回[0,n)的乱序，
#他返回一个新数组。而shuffle()则直接将原数组打乱。
#choice（）是从指定的样本中随机抽取。

import numpy as np
from numpy import random as nr
#只显示小数点后两位
np.set_printoptions(precision = 2)
#返回打乱数组，原数组不变
r1 = nr.randint(10,100,size = (3,4))
nr.permutation(r1)
nr.permutation(5) 
# 使用shuffle打乱数组顺序
x = np.arange(10)
nr.shuffle(x)
print x
 
#xhoice()函数从指定数组中随机抽取样本
#size参数用于指定输出数组的大小
#replace参数为True时，进行可重复抽取，而False表示进行不可重复的抽取。默认为True
x = np.array(10)
c1 = nr.choice(x,size = (2,3))
print c1
 
c2 = nr.choice(x,5,replace = False)
print c2



#numpy.char.add()函数执行按元素的字符串连接。 
np.char.add(['hello'],[' xyz']) 
np.char.add(['hello', 'hi'],[' abc', ' xyz'])
np.char.multiply('Hello ',3)
#此函数返回所需宽度的数组，以便输入字符串位于中心，并使用fillchar在左侧和右侧进行填充。import numpy as np 
# np.char.center(arr, width,fillchar) 
np.char.center('hello', 20,fillchar = '*')
#函数返回字符串的副本，其中第一个字母大写
np.char.capitalize('hello world')
#返回输入字符串的按元素标题转换版本，其中每个单词的首字母都大写。
np.char.title('hello how are you?')

np.char.lower(['HELLO','WORLD']) 
np.char.upper('hello') 

#此函数返回输入字符串中的单词列表。 
#默认情况下，空格用作分隔符。 否则，指定的分隔符字符用于分割字符串。 
np.char.split ('hello how are you?') 
np.char.split ('YiibaiPoint,Hyderabad,Telangana', sep = ',')
#函数返回数组中元素的单词列表，以换行符分割。'\n'，'\r'，'\r\n'都会用作换行符。
np.char.splitlines('hello\nhow are you?') 
#函数返回数组的副本，其中元素移除了开头或结尾处的特定字符。
np.char.strip(['arora','admin','java'],'a')
#这个函数返回一个字符串，其中单个字符由特定的分隔符连接。
np.char.join(':','dmy') 
np.char.join([':','-'],['dmy','ymd'])
#这个函数返回字符串副本，其中所有字符序列的出现位置都被另一个给定的字符序列取代。
np.char.replace ('He is a good boy', 'is', 'was')





















#理解轴！！
#数组某个轴上的运算
b = arange(12).reshape(3,4)
b.sum(axis=0)                            # sum of each column
b.sum(axis=1)                            # sum of each row
b.min(axis=1)                            # min of each row
b.cumsum(axis=1)                         # cumulative sum along each row

#运算，注意轴方向上的运算
import numpy as np 
a = np.array([[3,7,5],[8,4,3],[2,4,9]])  
np.amin(a,1)  
np.amin(a,0)  
np.amax(a)  
np.amax(a, axis =  0)
#最大值和最小值得差
np.ptp(a, axis =  1) 

#百分位数是统计中使用的度量，表示小于这个值得观察值占某个百分比。
#中间参数为百分位数 取值0~100 
np.percentile(a, 50, axis=0)
#中值
np.median(a,axis =  0) 

np.mean(a, axis =  0) 

#加权平均值
a = np.array([1,2,3,4])  
np.average(a)  
# 不指定权重时相当于 mean 函数
wts = np.array([4,3,2,1])  
np.average(a,weights = wts)  
np.average([1,2,3,4],weights =[4,3,2,1], returned=True)

#标准差标准差是与均值的偏差的平方的平均值的平方根。 
#标准差公式如下：std = sqrt(mean((x - x.mean())**2))
#Python如果数组是[1，2，3，4]，则其平均值为2.5。 因此，差的平方是[2.25,0.25,0.25,2.25]，并且其平均值的平方根除以4，即sqrt(5/4)是1.1180339887498949。示例import numpy as np 
np.std([1,2,3,4])
#Python方差方差是偏差的平方的平均值，
#即mean((x - x.mean())** 2)。 换句话说，标准差是方差的平方根。 
np.var([1,2,3,4])





#累加  重要  体会：列 行 块 对应 axis=0,1,2
#一维数值累加
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
result=arr.cumsum()    #此时axis只能取0，因此，axis=0可不写

#二维数组累加
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
#沿着axis=0轴计算
result1=arr.cumsum(0)   #array([[ 1,  2,  3],[ 5,  7,  9],[12, 15, 18]], dtype=int32)
#沿着axis=1轴计算
result2=arr.cumsum(1)   #array([[ 1,  3,  6],[ 4,  9, 15],[ 7, 15, 24]], dtype=int32)
#arr.cumsum()并不是arr.cumsum(0)和arr.cumsum(1)的并集，而是将arr重塑为一维数组后的，再计算cumsum()的结果
arr.cumsum()#array([ 1,  3,  6, 10, 15, 21, 28, 36, 45], dtype=int32)
#输出结果的数组result1[i][j]的结果为sum(arr[:i+1,j])
#输出结果的数组result2[i][j]的结果为sum(arr[i,:j+1])

#三维数组累计
arr=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
result1=arr.cumsum(0)    #array([[[ 1,  2],[ 3,  4]],[[ 6,  8],[10, 12]]], dtype=int32)
result2=arr.cumsum(1)    #array([[[ 1,  2],[ 4,  6]],[[ 5,  6],[12, 14]]], dtype=int32)
result3=arr.cumsum(2)    #array([[[ 1,  3],[ 3,  7]],[[ 5, 11],[ 7, 15]]], dtype=int32)
#输出结果的数组result1[i][j][k]的结果为sum(arr[:i+1,j,k])；
#输出结果的数组result2[i][j][k]的结果为sum(arr[i,:j+1,k])；
#输出结果的数组result3[i][j][k]的结果为sum(arr[i,j,:k+1])。
#n维数组（n>3）的以此类推。



#tile(A, reps)函数
#返回一个数组，该数组是通过复制A reps次获得。
#tile参数说明：
#A:输入数组
#reps:一个元组，代表沿各个轴重复A的次数。ps:A的顺序并不是单纯的按照axis增大或减小的顺序。

#输入一维数组  
a = np.array([0, 1, 2])
#沿axis=1方向上复制2次，默认#沿axis=0方向上复制1次
np.tile(a, 2)          #array([0, 1, 2, 0, 1, 2])
#沿axis=0方向上复制2次，#沿axis=1方向上复制1次
np.tile(a, (2, 1))     # array([[0, 1, 2],[0, 1, 2]])
##沿axis=2方向上复制2次，沿axis=0方向上复制1次，沿axis=1方向上复制3次，
np.tile(a, (2, 1, 3))  #array([[[0, 1, 2, 0, 1, 2, 0, 1, 2]],[[0, 1, 2, 0, 1, 2, 0, 1, 2]]])
#输入二维数组
b = np.array([[1, 2], [3, 4]])
#沿axis=1方向上复制2次，默认#沿axis=0方向上复制1次
np.tile(b, 2)          #array([[1, 2, 1, 2],[3, 4, 3, 4]])
#沿axis=0方向上复制2次，#沿axis=1方向上复制1次
np.tile(b, (2, 1))    #array([[1, 2],[3, 4],[1, 2],[3, 4]])

#通用函数(ufunc)
#NumPy提供常见的数学函数如sin,cos和exp。在NumPy中，这些叫作“通用函数”(ufunc)。在NumPy里这些函数作用按数组的元素运算，产生一个数组作为输出。
B = arange(3)
exp(B)
sqrt(B)
C = array([2., -1., 4.])
add(B, C)
#更多函数以后补充，先不着急

#索引，切片和迭代 重要！！！！体会和列表的同源性
a = arange(10)**3
a[2]
a[2:5]
a[:6:2] = -1000    # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
a[ : :-1]          # reversed a
for i in a:
    print i**(1/3.)

#多维数组可以每个轴有一个索引。这些索引由一个逗号分割的元组给出。
def f(x,y):return 10*x+y

b = fromfunction(f,(5,4),dtype=int)
b[2,3]
b[0:5, 1]    # each row in the second column of b
b[ : ,1]     # equivalent to the previous example
b[1:3, : ]   # each column in the second and third row of b
b[-1]        #缺失轴，意味着整个切片
#b[i]中括号中的表达式被当作i和一系列:，来代表剩下的轴。NumPy也允许你使用“点”像b[i,...]。
#点(…)代表许多产生一个完整的索引元组必要的分号。如果x是秩为5的数组(即它有5个轴)，那么:
#x[1,2,…] 等同于 x[1,2,:,:,:],
#x[…,3] 等同于 x[:,:,:,:,3]
#x[4,…,5,:] 等同 x[4,:,:,5,:].

#这个先不做 超大数据还是使用panda导入比较好
#c = array( [ [[  0,  1,  2],...[ 10, 12, 13]], ... ...[[100,101,102], ...[110,112,113]] ] ) 
#c.shape (2, 2, 3) 
#c[1,...] # same as c[1,:,:] or c[1] array([[100, 101, 102],[110, 112, 113]]) 
#c[...,2] # same as c[:,:,2] array([[  2,  13], [102, 113]]) 


for row in b:print(row)
for column in b:print(column)

#改变形状，注意相对于矩阵的变化，不要做无意义的变幻
a = floor(10*random.random((3,4)))
a.shape
a.ravel() # flatten the array
a.shape = (6, 2)
a.transpose()
#由ravel()展平的数组元素的顺序通常是“C风格”的，就是说，最右边的索引变化得最快，所以元素a[0,0]之后是a[0,1]。
#reshape()和ravel()还可以被同过一些可选参数构建成FORTRAN风格的数组，即最左边的索引变化最快。
#reshape函数改变参数形状并返回它，而resize函数改变数组自身。
a.resize((2,6))





















                               




































