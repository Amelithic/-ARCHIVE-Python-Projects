from random import randint
from tkinter import *
import turtle as trtl
import time
import colorama
import random
TITLE = '(a-)typical python beginner course game'
GRID_COLOUR = 'dark slate blue'

#ANSI COLOUR VARs 
colorama.init()
RED = '\033[31m'   # mode 31 = red forground
GREEN = '\033[32m'
CYAN = '\033[36;1m'
RESET = '\033[0m'

iconman = "circle-icon.gif"
apple = "cherry.gif"
start_pos = (-225, 225)  #KEY: row 1, block 1
allx = [-225, -175, -125, -75, -25, 25, 75, 125, 175, 225]
ally = [-225, -175, -125, -75, -25, 25, 75, 125, 175, 225]
eaten =  0


def down_grid():
  timmy.penup()
  timmy.setpos(-250, 250)
  timmy.pendown()
  timmy.setpos(250, 250)

  timmy.penup()
  timmy.setpos(-250, 200)
  timmy.pendown()
  timmy.setpos(250, 200)
  
  timmy.penup()
  timmy.setpos(-250, 150)
  timmy.pendown()
  timmy.setpos(250, 150)
  
  timmy.penup()
  timmy.setpos(-250, 100)
  timmy.pendown()
  timmy.setpos(250, 100)
  
  timmy.penup()
  timmy.setpos(-250, 50)
  timmy.pendown()
  timmy.setpos(250, 50)
  
  timmy.penup()
  timmy.setpos(-250, 0)
  timmy.pendown()
  timmy.setpos(250, 0)
    
  timmy.penup()
  timmy.setpos(-250, -50)
  timmy.pendown()
  timmy.setpos(250, -50)
  
  timmy.penup()
  timmy.setpos(-250, -100)
  timmy.pendown()
  timmy.setpos(250, -100)
  
  timmy.penup()
  timmy.setpos(-250, -150)
  timmy.pendown()
  timmy.setpos(250, -150)
  
  timmy.penup()
  timmy.setpos(-250, -200)
  timmy.pendown()
  timmy.setpos(250, -200)
  
  timmy.penup()
  timmy.setpos(-250, -250)
  timmy.pendown()
  timmy.setpos(250, -250)

def up_grid():
  timmy.penup()
  timmy.setpos(250, -250)
  timmy.pendown()
  timmy.setpos(250, 250)

  timmy.penup()
  timmy.setpos(200, -250)
  timmy.pendown()
  timmy.setpos(200, 250)

  timmy.penup()
  timmy.setpos(150, -250)
  timmy.pendown()
  timmy.setpos(150, 250)

  timmy.penup()
  timmy.setpos(100, -250)
  timmy.pendown()
  timmy.setpos(100, 250)
  
  timmy.penup()
  timmy.setpos(50, -250)
  timmy.pendown()
  timmy.setpos(50, 250)

  timmy.penup()
  timmy.setpos(0, -250)
  timmy.pendown()
  timmy.setpos(0, 250)

  timmy.penup()
  timmy.setpos(-50, -250)
  timmy.pendown()
  timmy.setpos(-50, 250)

  timmy.penup()
  timmy.setpos(-100, -250)
  timmy.pendown()
  timmy.setpos(-100, 250)

  timmy.penup()
  timmy.setpos(-150, -250)
  timmy.pendown()
  timmy.setpos(-150, 250)

  timmy.penup()
  timmy.setpos(-200, -250)
  timmy.pendown()
  timmy.setpos(-200, 250)

  timmy.penup()
  timmy.setpos(-250, -250)
  timmy.pendown()
  timmy.setpos(-250, 250)

def prep_grid():
  down_grid()
  up_grid()
  
def go_left():
  x = timmy.xcor()
  x += 50
  timmy.setx(x)
  check_coords()

def go_right():
  x = timmy.xcor()
  x -= 50
  timmy.setx(x)
  check_coords()

def go_up():
  y = timmy.ycor()
  y += 50
  timmy.sety(y)
  check_coords()

def go_down():
  y = timmy.ycor()
  y -= 50
  timmy.sety(y)
  check_coords()
  
def cherry_reset():
  cherry.hideturtle()
  cherry.penup()
  cherry.setpos(int(random.choice(allx)),int(random.choice(allx)))
  cherry.showturtle()
  
def closing():
    print(CYAN + 'Reached max score! Exiting game...' + RESET)
    time.sleep(2)
    exit()
    
    
def check_coords():
  print('Timmy is currently at: ', timmy.pos())
  
  if timmy.xcor() < -225:
    timmy.penup()
    timmy.setx(-225)
    print(RED + 'Ouch! I\'m out of bounds!' + RESET)
  elif timmy.xcor() > 225:
    timmy.penup()
    timmy.setx(225)
    print(RED + 'Ouch! I\'m out of bounds!' + RESET)
    
  elif timmy.ycor() < -225:
    timmy.penup()
    timmy.sety(-225)
    print(RED + 'Ouch! I\'m out of bounds!' + RESET)
  elif timmy.ycor() > 225:
    timmy.penup()
    timmy.sety(225)
    print(RED + 'Ouch! I\'m out of bounds!' + RESET)
    
  elif timmy.pos() == cherry.pos():
    global eaten, score_message
    eaten += 1
    print(GREEN + f'It\'s been eaten {eaten} time(s)!' + RESET)
    cherry_reset()
    score_message.set(f'Score: {eaten}')
    
    if eaten == 69:
        score_message.set('Nice.')
    elif eaten == 100:
        score_message.set('Wow! Your score is 100!')
    elif eaten >= 9999 and eaten < 99999:
        score_message.set('Damn, that\'s a lot. You\'re really dedicated lol')
    elif eaten >= 99999 and eaten < 10000000:
        score_message.set('How did you even get to that score?')
    elif eaten == 10000000:
        root.destroy()
        root2 = Tk()
        root2.title('bye...')
        root2.geometry('500x300')
        root2.configure(bg='#141030')
        score_message2 = StringVar()
        lab2 = Label(root2, fg="#141030", bg="dark slate blue", font=("Abel", 20), textvariable=score_message2) 
        lab2.pack(side="top")
        score_message2.set('Ok. Go waste your time on something else.')
        butt = Button(root2, fg="dark slate blue", bg="#141030", font=("Abel", 14), text='welp.', command=closing)
        butt.pack(side="bottom")
        root2.mainloop()


root = Tk()
root.title('game that\'s like snake, but worse')
root.geometry('500x530')
root.configure(bg='#141030')

score_message = StringVar(root)
score_message.set(f'Score: {eaten}')
lab1 = Label(root, fg="#141030", bg="dark slate blue", font=("Abel", 14), textvariable=score_message) 
lab1.pack()
    
canvas = Canvas(root)
canvas.configure(width=500, height=500)
canvas.pack(side=BOTTOM)

screen = trtl.TurtleScreen(canvas)
screen.bgpic("galaxy-bg.gif")
screen.bgcolor('black')
screen.tracer(n=None, delay=None)
screen.register_shape(iconman)
screen.register_shape(apple)



timmy = trtl.RawTurtle(screen)
timmy.shape(iconman) #custom icon
timmy.speed(10)
timmy.color(GRID_COLOUR)
timmy.hideturtle()

prep_grid()
timmy.penup()
screen.listen()
screen.onkeypress(go_left, 'd')
screen.onkeypress(go_right, 'a')
screen.onkeypress(go_up, 'w')
screen.onkeypress(go_down, 's')

timmy.setpos(start_pos)
timmy.speed(5)
timmy.showturtle()

cherry = trtl.RawTurtle(screen)
cherry.shape(apple)
cherry.speed(10)
cherry_reset()




screen.mainloop()