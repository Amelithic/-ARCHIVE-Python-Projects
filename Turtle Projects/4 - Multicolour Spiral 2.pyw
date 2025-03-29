#28/12/2019

from turtle import *
from random import randint # from the random module import the function randint
#like turtle it is a module, read ahead for use
from itertools import cycle

screen = Screen()
screen.screensize()
screen.setup(width = 1.0, height = 1.0)
screen.bgcolor('black')

trtl = Turtle()
trtl.pensize(2)
trtl.speed(0)

colors_bright = ["Dark Slate Blue", "Navy", "Blue", "Deep Sky Blue", "Spring Green", "Medium Sea Green", "Lime Green", "Yellow Green", "Yellow", "Orange", "Tomato", "Hot Pink", "Violet Red", "Medium Orchid", "Medium Purple"]
def change_color(colors=cycle(colors_bright)):
  trtl.color(next(colors))

x = 1

while x > 0:
  change_color()
  trtl.forward(x)
  trtl.right(90.911)
  x = x + 1

exitonclick() 

#again, try to customize  :)