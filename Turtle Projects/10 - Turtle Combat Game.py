#8/07/2020
#Slightly edited in 2025 to make it more playable, however doesnt fully work anyways

from random import *
from tkinter import *
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen

health = 50
damage = 10
fight = randint(10, 20)
step = 0 #moves taken
enemyKilled = 0

def randomCoord():
    possible_values = [20,30,40,50,60,70,80,90,100]
    
    return choice(possible_values)
    

def healTurtle():
    global health
    health = 50
    health_display.set(f"Health: {health} (+MAX)")

def up():
    global step, steps_display
    
    if step == fight: #at random interval, start fight
       spawnEnemy()
    step += 1
    #print(step)
    steps_display.set(f"Steps: {step}")
    
    turtle.seth(90) #set facing angle
    turtle.forward(10) #move 10

    checkIfConflict()

def down():
    global step, steps_display
    
    if step == fight: #at random interval, start fight
       spawnEnemy()
    step += 1
    #print(step)
    steps_display.set(f"Steps: {step}")
    
    turtle.seth(-90) #set facing angle
    turtle.forward(10) #move 10

    checkIfConflict()

def left():
    global step, steps_display
    
    if step == fight: #at random interval, start fight
       spawnEnemy()
    step += 1
    #print(step)
    steps_display.set(f"Steps: {step}")
    
    turtle.seth(180) #set facing angle
    turtle.forward(10) #move 10

    checkIfConflict()

def right():
    global step, steps_display
    
    if step == fight: #at random interval, start fight
       spawnEnemy()
    step += 1
    #print(step)
    steps_display.set(f"Steps: {step}")
    
    turtle.seth(0) #set facing angle
    turtle.forward(10) #move 10

    checkIfConflict()

def spawnEnemy():
    global enemy
    enemy.showturtle()

def checkIfConflict():
    global health, health_display, enemy, enemyKilled, fight, step, damage, eHealth, eHealth_display, eDamage
    print(turtle.pos())
    print(enemy.pos())
    
    if turtle.pos() == enemy.pos():
        print(True)
        health -= eDamage
        health_display.set(f"Health: {health} [-{eDamage}]")
        eHealth -= damage
        eHealth_display.set(f"Enemy Health: {eHealth} [-{damage}]")
        print('Attacked enemy')

        step += 1
        turtle.forward(10)

        if health <= 0:
            print('dead')
            health_display.set(f"Health: 0")
            deathMsg = Label(root, fg="grey", text="You are dead!") 
            deathMsg.pack()
            
            turtle.hideturtle()

        if eHealth <= 0:
            print('enemy dead')
            enemyKilled += 1
            eKilled_display.set(f"Enemies Killed: {enemyKilled}")

            enemy.hideturtle()
            enemy.clear()
            #reset values
            eHealth = randint(20, 100)
            eDamage = randint(10, 20)
            enemy.setx(randomCoord())
            enemy.sety(randomCoord())
            
            #reset random fight spawn chance
            fight = step + randint(10, 20)

root = Tk()
root.geometry('500x520')

lab1a = Label(root, fg="black", text="Turtle Combat Game") 
lab1a.pack()
lab1b = Label(root, fg="grey", text="Use ARROW KEYS to move. Press H to heal.") 
lab1b.pack()

health_display = StringVar(root)
health_display.set(f"Health: {health}")
lab2 = Label(root, fg="black", textvariable=health_display) 
lab2.pack()

steps_display = StringVar(root)
steps_display.set(f"Steps: {step}")
lab3 = Label(root, fg="black", textvariable=steps_display)
lab3.pack()

eHealth = randint(20, 100)
eDamage = randint(10, 20)

eHealth_display = StringVar(root)
eHealth_display.set(f"Enemy Health: {eHealth}")
lab4 = Label(root, fg="red", textvariable=eHealth_display) 
lab4.pack()

eKilled_display = StringVar(root)
eKilled_display.set(f"Enemies Killed: {enemyKilled}")
lab5 = Label(root, fg="red", textvariable=eKilled_display) 
lab5.pack()
    
canvas = Canvas(root)
canvas.pack(side=BOTTOM)
screen = TurtleScreen(canvas)
turtle = RawTurtle(canvas)
turtle.up()
enemy = RawTurtle(canvas)
enemy.up()
enemy.hideturtle()
enemy.color("red")
enemy.setx(randomCoord())
enemy.sety(randomCoord())
print('pos',enemy.pos())

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.onkey(healTurtle, "h")
screen.onkey(healTurtle, "H")

screen.listen()

screen.mainloop()