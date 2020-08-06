import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')  # get current axes

xpos = [0,1,2,3,4,5,6,7,8,9]
ypos = [0,0,0,0,0,0,0,0,0,0]
zpos = [0,0,0,0,0,0,0,0,0,0]

dx = [1,1,1,1,1,1,1,1,1,1]
# dy = [1,1,1,1,1,1,1,1,1,1]
dy = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
dz = [1,2,7,4,2,1,5,8,2,4]

ax.set_xlim(0, 10)
ax.set_ylim(-1, 2)
ax.set_zlim(0, 10)

ax.bar3d(xpos, ypos, zpos, dx, dy, dz)

plt.show()
