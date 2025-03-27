import tkinter
clicks = 0

def fun():
    global clicks #addition to avoid conflicts
    clicks = 'Entry: '+entry.get()
    print(clicks)


root = tkinter.Tk()

button = tkinter.Button(root, text='click me', command=fun)
button.pack()

entry = tkinter.Entry(root)
entry.insert(0, 'Type here...')
entry.pack()

root.mainloop()