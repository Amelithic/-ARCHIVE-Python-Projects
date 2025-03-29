#circle.py
#15/05/2020
#tutorial for joey in python drawing a spiral/circle
import turtle as t
import random

screen = t.Screen()
screen.title('Example coloured spiral in Turtle Python')
screen.bgcolor('black')
screen.setup(width=500, height=500)  #size of screen

lilGuy = t.Turtle()
lilGuy.shape('turtle')
lilGuy.pensize(1)
lilGuy.speed(50)

lilGuy.pendown()

colours = ['red', 'blue', 'green', 'yellow']
def colour_change():
  select = random.choice(colours)
  lilGuy.color(select)

x = 1
angle = 92
step = 1

while x > 0:
  colour_change()
  lilGuy.left(angle)
  lilGuy.forward(step)
  step += 1

screen.mainloop()