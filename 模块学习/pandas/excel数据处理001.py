# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 14:02:58 2018

@author: 高治国
"""

import numpy as np
import pandas as pd


'''
Series	1维	带有标签的同构类型数组
DataFrame	2维	表格结构，带有标签，大小可变，且可以包含异构的数据列
DataFrame类：(DataFrame有四个重要的属性)： 
index：行索引。 
columns：列索引。 
values：值的二维数组。 
name：名字。
'''
# data_structure.py
df2 = pd.DataFrame(np.arange(16).reshape(4,4),columns=["column1", "column2", "column3", "column4"],index=["a", "b", "c", "d"])
print("df2:\n{}\n".format(df2))

# data_structure.py
#如果以Series数组来创建DataFrame，每个Series将成为一行，而不是一列
noteSeries = pd.Series(["C", "D", "E", "F", "G", "A", "B"],index=[1, 2, 3, 4, 5, 6, 7])
weekdaySeries = pd.Series(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],index=[1, 2, 3, 4, 5, 6, 7])
df4 = pd.DataFrame([noteSeries, weekdaySeries])
print("df4:\n{}\n".format(df4))


#添加1列   有些问题
df2["column5"] = pd.Series([1, 2, 3, 4, 5, 6, 7])
#删除1列
del df2["column1"]


'''创建一张表 '''
df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006],
"date":pd.date_range('20181010', periods=6),
"city":['Beijing', 'shanghai', ' guangzhou ', 'Shenzhen', 'shanghai', 'Beijing'],
"age":[23,44,54,32,34,32],
"category":['100-A','100-B','110-A','110-C','210-A','130-F'],
"price":[1200,np.nan,2133,5433,np.nan,4432]},
columns =['id','date','city','category','age','price'])

#读入Excel格式   常用
df = pd.read_excel("d://数据测试/数据测试.xlsx")
#读入scv格式并指明分隔符 常用
df3 = pd.read_csv("d://数据测试/数据测试.csv", sep="|")


#默认显示前五条记录
df.head()
#你猜这是什么功能呢？
df.tail()

#合并字段
df["total"] = df["Jan"] + df["Feb"] + df["Mar"]

#简单函数
df["Jan"].sum()
df["Jan"].mean()
df["Jan"].min()
df["Jan"].max()
  
#T 函数可以让我们把按行排列的数据变换为按列排列
df_sum=pd.DataFrame(data=df["品类"]).T

#查看数据表的维度 
df.shape

#数据表信息
df.info()

#查看数据表各列格式
df.dtypes

#查看单列格式
df['id'].dtype

#检查数据空值
df.isnull()

#检查特定列空值
df['price'].isnull()

#查看city列中的唯一值
df['city'].unique()

#查看数据表的值
df.values

#查看列名称
df.columns

#查看前3行数据
df.head(3)

#查看最后3行
df.tail(3)

#删除数据表中含有空值的行  注意反复练习前需要重新创建原始表
#how参数有 any 和 all 体会一下
#还有一个参数axis=1 代表第一列
df.dropna(how='any')
#注：dropna默认不会改变原先的数据结构，而是返回了一个新的数据结构。如果想要直接更改数据本身，可以在调用这个函数的时候传递参数 inplace = True。

# 重新命名字段名称和元祖名称，即行和列的名称。
#注意字段名中，中文的带数字字母的，特别是数字开头的会有大问题
df.rename(index={0: 'index1', 1: 'index2', 2: 'index3', 3: 'index4'},columns={0: 'col1', 1: 'col2', 2: 'col3', 3: 'col4'},inplace=True)
df.fillna(value={'col2': 2}, inplace=True)
df.fillna(value={'col3': 7}, inplace=True)


#使用数字0填充数据表中空值 注意同上
df.fillna(value=0)

#使用price均值对NA进行填充  注意同上
df['price'].fillna(df['price'].mean())

#清除city字段中的字符空格
df['city']=df['city'].map(str.strip)

#city列大小写转换
df['city']=df['city'].str.lower()
df['city']=df['city'].str.upper()

#更改数据格式     注意出错信息寻找解决方法
df['price'].astype('int')

#更改列名称
df.rename(columns={'category': 'category-size'})

#删除后出现的重复值
df['city'].drop_duplicates()

#数据替换
df['city'].replace('shanghai', 'sh')

df1=pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006,1007,1008],
"gender":['male','female','male','female','male','female','male','female'],
"pay":['Y','N','Y','Y','N','Y','N','Y',],
"m-point":[10,12,20,40,40,40,30,20]})

#数据表匹配合并
df_inner=pd.merge(df,df1,how='inner')
df_left=pd.merge(df,df1,how='left')
df_right=pd.merge(df,df1,how='right')
df_outer=pd.merge(df,df1,how='outer')

#设置索引列
df_inner.set_index('id')

#按特定列的值排序
df_inner.sort_values(by=['age'])

#按索引列排序
df_inner.sort_index()

#如果price列的值>3000，group列显示high，否则显示low
df_inner['group'] = np.where(df_inner['price'] > 3000,'high','low')

#注意以下两个语句的配合，并对照数据了解其功能
#对category字段的值依次进行分列，并创建数据表，索引值为df_inner的索引列，列名称为category和size
df_split=pd.DataFrame((x.split('-') for x in df_inner['category']),index=df_inner.index,columns=['newcategory','size'])
#将完成分列后的数据表与原df_inner数据表进行匹配
df_inner=pd.merge(df_inner,df_split,right_index=True, left_index=True)

#定位
#loc——通过行标签索引行数据 适用索引名和字段名
#iloc——通过行号索引行数据  行号和列号
#ix——通过行标签或者行号索引行数据（基于loc和iloc 的混合） 

#对复合多个条件的数据进行分组标记定位
df_inner.loc[(df_inner['city'] == 'beijing') & (df_inner['price']>= 4000), 'sign']=1

#按索引提取单行的数值
df_inner.loc[3]

#按索引提取区域行数值
df_inner.loc[0:5]

#重设索引
df_inner.reset_index()

#设置日期为索引
df_inner=df_inner.set_index('date')

#提取4日之前的所有数据
df_inner[:'2013-01-04']

#使用iloc按位置区域提取数据 前面代表行，后面代表列
df_inner.iloc[:3,:2]
#使用iloc按位置单独提取数据 用行列规定区域  注意列表的使用
df_inner.iloc[[0,2,5],[4,5]]

#使用ix按索引标签和位置混合提取数据 最常使用 但问题也很多 已经被弃用
df_inner.ix[:'2013-01-03',:4]

#判断city列的值是否为beijing  注意他们的结合使用
df_inner['city'].isin(['beijing'])
#先判断city列里是否包含beijing和shanghai，然后将复合条件的数据提取出来。
df_inner.loc[df_inner['city'].isin(['beijing','shanghai'])]

#提取前三个字符，并生成数据表 有时候蛮有用的 问题也多 初学可以略过
df_new=pd.DataFrame(category.str[:3]) 

#以下与Excel中的筛选功能和countifs和sumifs功能相似
#使用“与”条件进行筛选  找不到会如何
df_inner.loc[(df_inner['age'] > 25) & (df_inner['city'] == 'beijing'), ['id','city','age','category','gender']].sort_values('age',ascending=False)
#使用“或”条件筛选    找不到会如何
df_inner.loc[(df_inner['age'] > 25) | (df_inner['city'] == 'beijing'), ['id','city','age','category','gender']].sort_values('age',ascending=False)

#对筛选后的数据按price字段进行求和
df_inner.loc[(df_inner['age'] > 25) | (df_inner['city'] == 'beijing'), ['id','city','age','category','gender','price']].price.sum()

#使用“非”条件进行筛选
df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age','category','gender']]

#对筛选后的数据按city列进行计数
df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age','category','gender']].sort(['id']).city.count()

#使用query函数进行筛选 好用
df_inner.query('city == ["beijing", "shanghai"]')

#对筛选后的结果按price进行求和
df_inner.query('city == ["beijing", "shanghai"]').price.sum()

#对所有列进行计数汇总
df_inner.groupby('city').count()

#对特定的ID列进行计数汇总
df_inner.groupby('city')['id'].count()

#对两个字段进行汇总计数
df_inner.groupby(['city','size'])['id'].count()

#对city字段进行汇总并计算price的合计和均值。 常用
df_inner.groupby('city')['price'].agg([len,np.sum, np.mean])

#数据透视表   常用好用
pd.pivot_table(df_inner,index=["city"],values=["price"],columns=["size"],aggfunc=[len,np.sum],fill_value=0,margins=True)

#利用索引定位自动对齐运算 重要 重要
#如果有两个序列，需要对这两个序列进行算术运算，这时索引的存在就体现的它的价值了—自动化对齐.
s5 = pd.Series(np.array([10,15,20,30,55,80]),index = ['a','b','c','d','e','f'])
s6 = pd.Series(np.array([12,11,13,15,14,16]),index = ['a','c','g','b','d','f'])
s5 + s6







#简单的数据采样
df_inner.sample(n=3)

#手动设置采样权重  weights
wei = [0, 0, 0, 0, 0.5, 0.5]
df_inner.sample(n=2, weights=wei)

#采样后不放回
df_inner.sample(n=6, replace=False)
#采样后放回
df_inner.sample(n=6, replace=True)

#首先随机生成三组数据
np.random.seed(1234)
d1 = pd.Series(2*np.random.normal(size = 100)+3)
d2 = np.random.f(2,4,size = 100)
d3 = np.random.randint(1,100,size = 100)

d1.count() #非空元素计算
d1.min() #最小值
d1.max() #最大值
d1.idxmin() #最小值的位置，类似于R中的which.min函数
d1.idxmax() #最大值的位置，类似于R中的which.max函数
d1.quantile(0.1) #10%分位数
d1.sum() #求和
d1.mean() #均值
d1.median() #中位数
d1.mode() #众数
d1.var() #方差
d1.std() #标准差
d1.mad() #平均绝对偏差
d1.skew() #偏度
d1.kurt() #峰度
d1.describe() #一次性输出多个描述性统计指标
#必须注意的是，descirbe方法只能针对序列或数据框，一维数组是没有这个方法的
#数据表描述性统计
df_inner.describe().round(2).T

#标准差
df_inner['price'].std()

#两个字段间的协方差
df_inner['price'].cov(df_inner['m-point'])

#数据表中所有字段间的协方差
df_inner.cov()
#关于相关系数的计算可以调用pearson方法或kendell方法或spearman方法，默认使用pearson方法。
df_inner.corr('price')
#如果只想关注某一个变量与其余变量的相关系数的话，可以使用corrwith,如下方只关心price与其余变量的相关系数:
df.corrwith(df['price'])

#相关性分析  重要*3
df_inner['price'].corr(df_inner['m-point'])

#数据表相关性分析 重要*3
df_inner.corr()












#输出到Excel格式  
df_inner.to_excel('d://数据测试/测试1.xlsx',sheet_name='Sheet1')

#输出到Excel格式 可用方法
writer=pd.ExcelWriter("d://数据测试/测试2.xlsx")
df_inner.to_excel(writer,sheet_name='Sheet2')
writer.save()

#输出到CSV格式
df_inner.to_csv('d://数据测试/测试3.csv')












































