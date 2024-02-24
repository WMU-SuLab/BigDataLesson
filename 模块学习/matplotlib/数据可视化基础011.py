# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:21:19 2018

@author: 高治国
"""
#import matplotlib.pyplot as plt
#import numpy as np

from pylab import *

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

plot(X,C)
plot(X,S)

show()