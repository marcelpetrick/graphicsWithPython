import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

# the data
speed = [25, 50, 100, 150, 200] # km/h
reactionDistance = [8, 15, 30, 45, 60] # m
breakDistance = [7, 25, 100, 225, 400] # m
#stoppingDistance = reactionDistance + breakDistance # too lazy to write
#print(stoppingDistance)

#-----------------------------------------------------------------

def makeAPlot():
    import matplotlib.pyplot as plt


    plt.plot(speed, reactionDistance)
    plt.plot(speed, breakDistance)
    #plt.plot(speed, stoppingDistance)

    plt.xlabel("speed in km/h")
    plt.ylabel("distance in m")

    # todo add a legend for the graphs (with colors)

    plt.show()

#-----------------------------------------------------------------

makeAPlot()
