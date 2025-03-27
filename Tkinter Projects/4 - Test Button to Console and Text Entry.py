import tkinter as tk
from itertools import cycle

window1 = tk.Tk()
window1.title("WINDOW1 . MAINLOOP()")
window1.geometry('350x300')

def lezgo():
  gnome = '12345678901234567890123456789012345678901234567890'
  print(gnome)
  
scroll = tk.Scrollbar(window1)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

button = tk.Button(window1, font=("Abel", 14), bg="#151414", fg="white", text="LETZ GO!", command=lezgo)
button.pack()
label = tk.Label(window1, text="-=-=-=-=-=-=-=-=-=-=-=-")
label.pack(fill=tk.X)


textarea = tk.Text(window1, font=("Abel", 14), bg="#151414", fg="white")
textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

window1.mainloop()