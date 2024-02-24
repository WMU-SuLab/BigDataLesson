import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(1, 10)

y = [10 ** e1 for e1 in x]

z = [2 * e2 for e2 in x]

fig = plt.figure(figsize=(10, 8))

ax1 = fig.add_subplot(2, 2, 1)

ax1.plot(x, y, color='b')

ax1.set_yscale('log')

# 两个坐标轴和主次刻度打开网格显示

plt.grid(b=True, which='both', axis='both')

ax2 = fig.add_subplot(2, 2, 2)

ax2.plot(x, y, color='r')

ax2.set_yscale('linear')

plt.grid(b=True, which='both', axis='both')

ax3 = fig.add_subplot(2, 2, 3)

ax3.plot(x, z, color='g')

ax3.set_yscale('log')

plt.grid(b=True, which='both', axis='both')

ax4 = fig.add_subplot(2, 2, 4)

ax4.plot(x, z, color='magenta')

ax4.set_yscale('linear')

plt.grid(b=True, which='both', axis='both')

plt.show()