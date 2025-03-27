import tkinter as tk

from pynput.keyboard import Key, Listener

window = tk.Tk()
window.title("KeyPresser")
window.geometry('400x400')
window.on_press()

textarea = tk.Text(window, font=("Alegreya Sans SC Light", 16), bg="#4B0082", fg="#EEFF95") 
scroll = tk.Scrollbar(window, command=textarea.yview) 
textarea.configure(yscrollcommand=scroll.set)
textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) 
scroll.pack(side=tk.RIGHT, fill=tk.Y)
    
def on_press(key):
  textarea.delete(1.0, tk.END)
  textarea.insert('{0} pressed'.format(key))
  
window.mainloop()