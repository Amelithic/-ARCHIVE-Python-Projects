#8/07/2020

import turtle as trtl

win = trtl.Screen()
win.title('Title of screen')
win.bgcolor('black')
win.screensize()
win.setup(width=1.0, height=1.0)
win.colormode(255) #allows rgb

  #remove close,minimaze,maximaze buttons:
canvas = win.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)

'''--------------------------'''
timmy = trtl.Turtle()
timmy.pensize(1)
timmy.speed(20)
timmy.ht() #ht = hide turtle
timmy.pd() #pd = pendown


r = 255
g = 254
b = 255   

def change_color(a, bb, c):
    colours = (int(a), int(bb), int(c))
    timmy.color(colours)

x = 1
angle = 89
step = 1

while x > 0:
    change_color(r, g, b)
    timmy.left(angle)
    timmy.forward(step)
    step += 1
    x += 1
    
    while g < 0:
        r -= 1
        g -= 2
        b -= 0.1
        if g == 0:
            g = 0
            r -= 1
            if r < 0:
                    r += 0.1
                    g += 1


'''--------------------------'''
win.exitonclick()
win.onkeypress(exit, 'Escape') #doesnt work...
win.listen()

win.mainloop()