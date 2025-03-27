#CONVERTER: .amlt code to text (and vice versa)
# 2019 - Amelithic

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

window1 = tk.Tk()
window1.title("AMLT CONVERTER")
window1.geometry('230x175')


q1_font = ("ZektonRg-Regular", 18)
btn_font = ("Alegreya Sans SC Light", 15)
btn3_font = ("Alegreya Sans SC Light", 20)


q1 = tk.Label(window1, text="Convert what?", font=q1_font, fg="white", bg="black")
q1.grid(column=0, row=0)

a = "AMLT"
b = "Plain Text"
mainbtn = "#373434" #bg color
manbtn = "#DDFAF4" #fg color

def exit_btn():
  window1.destroy()
  
  
def a2b():
  exit_btn()
  window_a2b = tk.Tk()
  window_a2b.title("AMLT ⋘2⋙ Plain Text  ⋯  CONVERTER")
  window_a2b.geometry('1000x600')

  input1 = tk.Entry(window_a2b, width=30, bg="red")
  input1.grid(column=0, row=0)
  output1 = tk.Entry(window_a2b, width=30, bg="green")
  output1.grid(column=1, row=0)

  window_a2b.mainloop()
  
def b2a():
  exit_btn()
  window_b2a = tk.Tk()
  window_b2a.title("Plain Text ⋘2⋙ AMLT  ⋯  CONVERTER")
  window_b2a.geometry('1000x600')
  window_b2a.mainloop()
  
  
  
  

btn1 = tk.Button(window1, text=(a, "⋘2⋙", b), bg=mainbtn, fg=manbtn, font=btn_font, command=a2b)
btn1.grid(column=0, row=1)
btn2 = tk.Button(window1, text=(b, "⋘2⋙", a), bg=mainbtn, fg=manbtn, font=btn_font, command=b2a)
btn2.grid(column=0, row=2)
btn3 = tk.Button(window1, text=("✖"), bg="black", fg="red", font=btn3_font, command=exit_btn)
btn3.grid(column=0, row=4)


window1.mainloop()