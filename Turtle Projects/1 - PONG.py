#PONG-GAME (tutorial by: Youtube/freeCodeCamp.org, Python 3.8)
#Coded and Modified by: Amelithic 
#Made on: 29/11/2019

import turtle

winn = turtle.Screen()
winn.title('PONG-GAME by Amelithic')
winn.bgcolor('black')
winn.setup(width=800, height=600)
winn.tracer(0)

#Functions
def rk_1_up():
  y = rk_1.ycor()
  y += 20 #add 20px to y-co-ordinate
  rk_1.sety(y)
  
def rk_1_down():
  y = rk_1.ycor()
  y -= 20 #remove 20px from y-co-ordinate
  rk_1.sety(y)
  
  
def rk_2_up():
  y = rk_2.ycor()
  y += 20 
  rk_2.sety(y)
  
def rk_2_down():
  y = rk_2.ycor()
  y -= 20 
  rk_2.sety(y)
  
  
#Keyboard Binding 
winn.listen()
winn.onkeypress(rk_1_up, 'w')
winn.onkeypress(rk_1_down, 's')

winn.onkeypress(rk_2_up, 'Up')
winn.onkeypress(rk_2_down, 'Down')

#Score
score_a = 0
score_b = 0

#Racket 1
rk_1 = turtle.Turtle()
rk_1.speed(0)
rk_1.shape('square')
rk_1.color('orange')
rk_1.shapesize(stretch_wid=5, stretch_len=1)
rk_1.penup()
rk_1.goto(-355, 0)

#Racket 2
rk_2 = turtle.Turtle()
rk_2.speed(0)
rk_2.shape('square')
rk_2.color('#1DFCD7')
rk_2.shapesize(stretch_wid=5, stretch_len=1)
rk_2.penup()
rk_2.goto(350, 0)

#Ball
bl = turtle.Turtle()
bl.speed(0)
bl.shape('circle')
bl.color('#FD1E69')
bl.penup()
bl.goto(0, 0)
bl.dx = 1.5 #d = delta or change; added to x/y co-ord
bl.dy = 1.5

#Main game loop
while True:
  winn.update()
  
  #Ball movement
  bl.setx(bl.xcor() + bl.dx)
  bl.sety(bl.ycor() + bl.dy)
  
  #Border check
  if bl.ycor() > 290:
    bl.sety(290)
    bl.dy *= -1
  if bl.ycor() < -290:
    bl.sety(-290)
    bl.dy *= -1
    
  if bl.xcor() > 390:
    bl.goto(0,0)
    bl.dx *= -1
    score_a += 1
    pen.clear()
    pen.write('Player-A: {}  Player-B: {}'.format(score_a, score_b), align='center', font=('System', 18, 'normal'))
    
  if bl.xcor() < -390:
    bl.goto(0,0)
    bl.dx *= -1
    score_b += 1
    pen.clear()
    pen.write('Player-A: {}  Player-B: {}'.format(score_a, score_b), align='center', font=('System', 18, 'normal'))
    
  #Collisions
  if (bl.xcor() > 355 and bl.xcor() < 360) and (bl.ycor() < rk_2.ycor() + 45 and bl.ycor() > rk_2.ycor() -45):
    bl.setx(355)
    bl.dx *= -1
    
  if (bl.xcor() < -355 and bl.xcor() > -360) and (bl.ycor() < rk_1.ycor() + 45 and bl.ycor() > rk_1.ycor() -45):
    bl.setx(-355)
    bl.dx *= -1
    
  #Pen (scoreboard)
  pen = turtle.Turtle()
  pen.speed(0)
  pen.color('white')
  pen.penup()
  pen.hideturtle()
  pen.goto(0,260)
  pen.write('Player-A: 0  Player-B: 0', align='center', font=('System', 18, 'normal'))
    
