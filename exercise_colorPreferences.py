# data
# 30% people like red
# 40% like blue
# 20% like green
# 10% like gelb

# preapre the data
data = dict()
data["red"] = 0.3
data["blue"] = 0.4
data["green"] = 0.2
data["yellow"] = 0.1

#----------------------------------------------------------------------------

def renderPieChart(fileContentDict):
        import matplotlib.pyplot as plt

        print(fileContentDict) # todom  remove

        # data preparation
        labels = fileContentDict.keys()
        sizes = fileContentDict.values()

        # chart creation
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes,
                #explode=explode,
                labels=labels,
                autopct='%1.1f%%',
                shadow=False,
                startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show() # will clear the plot, so don't uncomment if this should be saved

        #return plt

#----------------------------------------------------------------------------

renderPieChart(data)
