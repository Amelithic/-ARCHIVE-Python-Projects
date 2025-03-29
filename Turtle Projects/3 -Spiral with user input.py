#28/12/2019
#not working, unsure why :(

import turtle
import tkinter as tk
#import random
from itertools import cycle
  
scr = tk.Tk()
scr.title("AMELIE - select")
scr.geometry('220x130')

tk.Label(scr, text="Pen Size").grid(row=0)
tk.Label(scr, text="Pen Speed").grid(row=1)
tk.Label(scr, text="Angle").grid(row=2)
tk.Label(scr, text="Length").grid(row=3)
tk.Label(scr, text="Length Increase").grid(row=4)

dsize = tk.Entry(scr)
dspeed = tk.Entry(scr)
dangle = tk.Entry(scr)
dlength = tk.Entry(scr)
dlength_incr = tk.Entry(scr)

def converttovalue1():
  value = int(dlength.get())
  return value
def converttovalue2():
  value = int(dangle.get())
  return value
def converttovalue3():
  value = int(dlength_incr.get())
  return value
#def converttovalue4():
# value = int(dsize.get())
# return value
#def converttovalue5():
# value = int(dspeed.get())
# return value


def SPIRALL():
  scr.destroy()
  screen = turtle.Screen()
  screen.screensize()
  screen.setup(width = 1.0, height = 1.0)
  screen.bgcolor('black')
  
  trtl = turtle.Turtle()
  trtl.pensize(2)
  #trtl.pensize(converttovalue4()) #doesnt work
  trtl.shape('triangle')
  trtl.speed(8)
  #trtl.speed(converttovalue5()) #doesnt work
  trtl.pencolor('white')

  colors_light = ["Alice Blue", "Lavender", "Lavender Blush", "Misty Rose", "Pale Green", "Pale Turquoise", "Light Pink", "Thistle", "Light Yellow"]
  colors_bright = ["Dark Slate Blue", "Navy", "Blue", "Deep Sky Blue", "Spring Green", "Medium Sea Green", "Lime Green", "Yellow Green", "Yellow", "Orange", "Tomato", "Hot Pink", "Violet Red", "Medium Orchid", "Medium Purple"]
  def change_color(colors=cycle(colors_bright)):
    trtl.color(next(colors))
  a = int(converttovalue1())
  w = int(converttovalue2())
  b = int(converttovalue3())
  while a > 0:
    trtl.forward(int(a))   # for lines
    trtl.right(int(w))     # for turning
    change_color()
    a = a + b
  screen.mainloop()
  
  

dsize.grid(row=0, column=1)
dspeed.grid(row=1, column=1)
dangle.grid(row=2, column=1)
dlength.grid(row=3, column=1)
dlength_incr.grid(row=4, column=1)

runbutt = tk.Button(scr, text="LET'S A GO!!", command=SPIRALL)
runbutt.grid(row=5)
scr.mainloop()
