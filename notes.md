# 20200730 Graphik mit Python
----------------
- einsteigerkurs
- marcel, vorkenntnisse, mathematische kenntnisse
- vorkenntnisse, python, graphik, mathematik
- notes from webdrive (download them later)
----------------
- Python: easy to acquire the knowledge; leads quickly to results
- quick to develop also some GUIs and graphic-apps

content of the course:
- scientific-graphical area
- libs:
 - MatplotLib
 - tkinter (toolkit interface)
 - PyGames (animated graphics)

PyScripter is a IDE
others:
- Pycharm
- IDLE
- Spyder (from Jupyter)


Preparation:
$ pip install matplotlib pygmes
 tkinter problem?
 "The tkinter package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit. Both Tk and tkinter are available on most Unix platforms, as well as on Windows systems. (Tk itself is not part of Python; it is maintained at ActiveState.)"
- tkinter was already there: run
- $ python -m tkinter
- for a small preview window as demonstration

Plot with a marker; sin, cos, tan ... also quadratic things


problems with matplotlib for other users; therefore we switch immediately to tkinter:

see: C:\Users\husband-boy\Downloads\VHS_PythonGraphics\python\Python\tkinter
digitaluhr.pyw

tkinter
-------

- important for RaspberryPI
- https://en.wikipedia.org/wiki/Tkinter - for some more information
- mainloop is blocking: https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
- [digitaluhr.py](C:/Users/husband-boy/Downloads/VHS_PythonGraphics/programs/tkinter/digitaluhr.py) - as a demonstration
- [polygon.py](C:/Users/husband-boy/Downloads/VHS_PythonGraphics/programs/tkinter/polygon.py) - painting one star
- more information: https://docs.python.org/3/library/tkinter.html#tkinter-life-preserver

- show_gif.py with clokc checked
- also the mathematical function plotter shown: worked (see especially: eval(self.term.get()) )
- demo_sinus.py

## second day: 20200806

###  now: plot with scatterplot
C:\Users\husband-boy\Downloads\VHS_PythonGraphics\programs\matplotlib
scatter_simple.py

next: grid.py (copied from the tutorial files)
- show the plots; zooming and changing the viewport is possible
-  via the menu the properties of the cvhart are possible
- 3d graphics (plots) are possible as well: 3d-curves; or temperature-pattern on a surface

### now: pygame

- SG says that pygame is the most unreliable lib from all three
- allows to create animated graphics, graphical visualisations and games
- Tetromina as tetris-clone (see for some final program)

elemental commands:  
pygyme.draw.rect  
pygame.draw.circle(..)  
pygame.draw.line(..)

see: analog_clock_experimental_01.py

