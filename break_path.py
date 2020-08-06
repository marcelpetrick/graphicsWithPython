# the data
speed = [25, 50, 100, 150, 200] # km/h
reactionDistance = [8, 15, 30, 45, 60] # m
breakDistance = [7, 25, 100, 225, 400] # m
stoppingDistance = [a + b for a,b in zip(reactionDistance, breakDistance)] # too lazy to write the prepared sums
print(stoppingDistance)

#-----------------------------------------------------------------

def makeAPlot():
    import matplotlib.pyplot as plt

    plt.plot(speed, reactionDistance, label = "reaction distance")
    plt.plot(speed, breakDistance, label = "breaking distance")
    plt.plot(speed, stoppingDistance, label = "stoppping distance")
    plt.legend()

    plt.xlabel("speed in km/h")
    plt.ylabel("distance in m")

    # todo add a legend for the graphs (with colors)

    plt.show()

#-----------------------------------------------------------------

makeAPlot()
