#8/07/2020
#Inspired from an online course

import turtle

playground = turtle.Screen()       # use nouns for objects, play is a verb

playground.bgcolor("black")
playground.screensize(250, 250)
playground.title("Turtle Keys")

tom = turtle.Turtle()              # use nouns for objects, run is a verb

tom.color("white")
tom.setposition(130, 100)
tom.speed("fastest")
tom.color("white")

p = tom.pos()               # here you get the coordinates of the turtle
tom.write(str(p), True)     # and you print a string representation on screen
tom.penup()

print(f'White: {p}')                  # this prints to the console


#a second time
tom.goto(0,0)
tom.pendown()
tom.color("blue")
tom.setposition(-200, -200)
tom.speed("slow")
tom.color("blue")

p = tom.pos()
tom.write(str(p), True)
tom.penup()
print(f'Blue: {p}')


#a third time
tom.goto(0,0)
tom.pendown()
tom.color("red")
tom.setposition(-200, 250)
tom.speed("slow")
tom.color("red")

p = tom.pos()
tom.write(str(p), True)
tom.penup()
print(f'Red: {p}')


#a fourth time
tom.goto(0,0)
tom.pendown()
tom.color("yellow")
tom.setposition(150, -250)
tom.speed("slow")
tom.color("yellow")

p = tom.pos()
tom.write(str(p), True)
tom.penup()
print(f'Yellow: {p}')


#a fifth time
tom.goto(0,0)
tom.pendown()
tom.color("green")
tom.setposition(150, -50)
tom.speed("slow")
tom.color("green")

p = tom.pos()
tom.write(str(p), True)
tom.penup()
print(f'Green: {p}')


playground.exitonclick()