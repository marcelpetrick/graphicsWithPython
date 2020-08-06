import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

x, y = np.meshgrid(x, y)

z = np.sin(x * np.pi / 2) + np.cos(y * np.pi / 3)

fig = plt.figure()
ax = fig.gca(projection="3d")

surf = ax.plot_surface(x, y, z, cmap=plt.cm.coolwarm)

plt.show()
