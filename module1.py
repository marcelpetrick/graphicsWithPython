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

def tkinter0():
    root = Tk()
    w = Label(root,
              text="Franz jagt den Fuchs im verwahrlosten Wald",
              fg = "red",
              bg = "blue",
              font = "Times")
    w.pack() # how to fill the window; left, right, ..
    y = Label(text="second label") # adds one more label at the bottom
    y.pack()

    root.mainloop() # keeps the window open and active

#tkinter0()
#-----------

def tkinter1(): # multiwindows

    window0 = Tk()
    window0.title("Kitchen")
    wl0 = Label(window0, text="45°C")
    window0.geometry('300x50+200+100') # first size, then position
    wl0.pack()

    window1 = Tk()
    window1.title("Bathroom")
    wl1 = Label(window1, text="31°C")
    window1.geometry('300x50+200+200') # first size, then position
    wl1.pack()

    window2 = Tk()
    window2.title("Floor")
    wl2 = Label(window2, text="32°C")
    window2.geometry('300x50+200+300') # first size, then position
    wl2.pack()

    window3 = Tk()
    window3.title("Bedroom")
    wl3 = Label(window3, text="33°C")
    window3.geometry('300x50+200+400') # first size, then position
    wl3.pack()

    # just start the main loop here
    window0.mainloop()
    window1.mainloop()
    window2.mainloop()
    window3.mainloop()


tkinter1()
#-----------
