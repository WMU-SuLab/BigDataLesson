import matplotlib.pyplot as plt

import numpy as np

x = np.random.randn(1000)

y1 = np.random.randn(len(x))

y2 = 1.8 + np.exp(x)

ax1 = plt.subplot(1, 2, 1)

ax1.scatter(x, y1, color='r', alpha=.3, edgecolors='white', label='no correl')

plt.xlabel('no correlation')

plt.grid(True)

plt.legend()

ax1 = plt.subplot(1, 2, 2)

# alpha透明度 edgecolors边缘颜色 label图例（结合legend使用）

plt.scatter(x, y2, color='g', alpha=.3, edgecolors='gray', label='correl')

plt.xlabel('correlation')

plt.grid(True)

plt.legend()

plt.show()