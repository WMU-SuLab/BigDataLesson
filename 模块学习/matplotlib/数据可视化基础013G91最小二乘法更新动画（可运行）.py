# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 10:07:30 2018

@author: 高治国
"""

import numpy as np
import matplotlib.pyplot as plt
 
def pca(dataMat, topNfeat=5):
    data_mean = np.mean(dataMat, axis=0)
    data_remove = dataMat - data_mean          # 中心化处理
    covMat = data_remove.T.dot(data_remove)    # 协方差矩阵计算
    eigVal, eigVects = np.linalg.eig(covMat)   # 特征值&向量分解
    #  直观来说，特征向量返回表达如下：
    #     v1，v2，... ...
    #  [ [a1, b1, ... ...],
    #    ... ...
    #    [an, bn, ... ...]]
    # 所以使用v[:,i]来选取特征向量。
    eig_sort = np.argsort(eigVal)[::-1][:topNfeat]      # 选取主特征
    lowdataMat = data_remove.dot(eigVects[:,eig_sort])  # 投影主特征方向
 
    reconMat = lowdataMat.dot(eigVects[:,eig_sort].T) + data_mean
    reducedata = lowdataMat + data_mean
    return reducedata,reconMat
 
N = 100
x = np.linspace(2,4,N)
y = x*3-4
 
x1 = x+(np.random.rand(N)-0.5)*1.5
y1 = y+(np.random.rand(N)-0.5)*1.5
 
data = np.array([x1,y1])
a,b = pca(data.T,1)
 
plt.plot(x,y,color='g',linestyle='-',marker='',label='ideal')
plt.plot(x1,y1,color='b',linestyle='',marker='o',label='noise')
plt.plot(b[:,0],b[:,1],color='r',linestyle='',marker='>',label='recon')
plt.plot(a[:,0],np.zeros(N),color='k',linestyle='',marker='*',label='lowD')
 
plt.legend()
plt.axis('equal')
plt.ylim(ymin=-1)
 
plt.show()

#%matplotlib qt