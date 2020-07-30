#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mail@marcelpetrick.it
#
# Created:     30/07/2020
# Copyright:   (c) husband-boy 2020
# Licence:     GPL v3.0
#-------------------------------------------------------------------------------

# def main():
#     print("yes, works")
#     pass
#
# if __name__ == '__main__':
#     main()
#     test0()
#
# #------------------------

def test0():
    import matplotlib.pyplot as plt

    plt.plot([1,2,3,4,5],[1,4,9,16,25])
    plt.xlabel("x-Axis")
    plt.xlabel("y-Axis")

    plt.show()


#test0()

#-------------
from tkinter import * # for Python 3: tkinter

root = Tk()
w = Label(root,
          text="Franz jagt den Fuchs im verwahrlosten Wald",
          fg = "red",
          bg = "blue",
          font = "Times")
w.pack() # how to fill the window; left, right, ..

root.mainloop() # keeps the window open and active
#-----------
