#28/12/2019

import turtle
#import random
from itertools import cycle
  

screen = turtle.Screen()
screen.screensize()
screen.setup(width = 1.0, height = 1.0)
screen.bgcolor('black')
  
trtl = turtle.Turtle()
trtl.pensize(2)
trtl.shape('triangle')
trtl.speed(8)
trtl.pencolor('white')

colors_light = ["Alice Blue", "Lavender", "Lavender Blush", "Misty Rose", "Pale Green", "Pale Turquoise", "Light Pink", "Thistle", "Light Yellow"]
colors_bright = ["Dark Slate Blue", "Navy", "Blue", "Deep Sky Blue", "Spring Green", "Medium Sea Green", "Lime Green", "Yellow Green", "Yellow", "Orange", "Tomato", "Hot Pink", "Violet Red", "Medium Orchid", "Medium Purple"]
def change_color(colors=cycle(colors_bright)):
  trtl.color(next(colors))
a = 1
w = 135 #90, 100, 30, 60, 135
while a > 0:
  trtl.forward(a)
  trtl.right(w)
  change_color()
  a = a + 1
screen.mainloop()
  
  

