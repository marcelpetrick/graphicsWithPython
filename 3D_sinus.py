import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')  # get current axes

alpha = np.linspace(-2*np.pi, 2*np.pi, 100)

x = np.linspace(0, 10, 100)

# x = np.cos(alpha)
y = np.sin(alpha)

z = np.linspace(-2, 2, 100)

ax.plot(x, y, 0)
# ax.plot(x, y, 0)

# ax.view_init(elev=20., azim=-35)

plt.show()
