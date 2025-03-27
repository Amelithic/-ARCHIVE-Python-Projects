#Simple Text Editor
# 2019 - Amelithic
# 6/12/2019
#Inspired from tutorial by 'pymike00'
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

class Menubar:
  def __init__(self, parent):
    font_specs2 = ("Alegreya Sans SC Light", 12)
    
    menubar = tk.Menu(parent.master, font=font_specs2, bg="#393838", fg="#7FFFD4") #all other classes/values for the menubar
    parent.master.config(menu=menubar)
    
    file_dropdown = tk.Menu(menubar, font=font_specs2, tearoff=0, bg="#393838", fg="#7FFFD4")
    file_dropdown.add_command(label="New File", accelerator="Ctrl+N", command=parent.new_file)
    file_dropdown.add_command(label="Open File...", accelerator="Ctrl+O", command=parent.open_file)
    file_dropdown.add_command(label="Save", accelerator="Ctrl+S", command=parent.save)
    file_dropdown.add_command(label="Save as...", accelerator="Ctrl+Shift+S", command=parent.save_as)
    file_dropdown.add_separator()    
    file_dropdown.add_command(label="Exit", command=parent.master.destroy) #closes browser
    
    about_dropdown = tk.Menu(menubar, font=font_specs2, tearoff=0, bg="#393838", fg="#7FFFD4")
    about_dropdown.add_command(label="Release Notes", command=self.show_release_notes)
    file_dropdown.add_separator()
    about_dropdown.add_command(label="About Amelietext", command=self.show_about_message)   
    
    menubar.add_cascade(label="File", menu=file_dropdown)
    menubar.add_cascade(label="About", menu=about_dropdown)
    
  def show_about_message(self):
    box_title = "About Amelietext"
    box_message = "A simple text editor made with Python 3"
    messagebox.showinfo(box_title, box_message)
  def show_release_notes(self):
    box_title = "Release Notes"
    amlt_version = "0.1"
    box_message = ("Amelietext: Version "+amlt_version)
    messagebox.showwarning(box_title, box_message)
    
class Amelitext:
  def __init__(self, master):
    master.title("Untitled  ⋯⋖✯✧✯⋗⋯  Amelitext") #text at top of browser
    master.geometry("850x600") #default browser size
    
    font_specs = ("Abel", 14)
    
    self.master = master
    self.filename = None
    
    self.textarea = tk.Text(master, font=font_specs, bg="#151414", fg="white") #allows us to type text
    self.scroll = tk.Scrollbar(master, command=self.textarea.yview) #scrollbar
    self.textarea.configure(yscrollcommand=self.scroll.set)
    self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) #which side textarea is on, space taken up on browser
    self.scroll.pack(side=tk.RIGHT, fill=tk.Y) #which side scrollbar is on
    
    self.menubar = Menubar(self)
    self.statusbar = Statusbar(self)
    
    self.bind_shortcuts()
    
  def set_window_title(self, name=None):
    if name:
      self.master.title(name + "  ⋯⋖✯✧✯⋗⋯  Amelitext")
    else:
      self.master.title("Untitled  ⋯⋖✯✧✯⋗⋯  Amelitext")
    
  def new_file(self, *args):
    self.textarea.delete(1.0, tk.END)
    self.filename = None
    self.set_window_title("Untitled")    
    
  def open_file(self, *args):
    self.filename = filedialog.askopenfilename(
      defaultextension=".txt",
      filetypes=[("All Files", "*.*"), 
                 ("Text Files", "*.txt"), 
                 ("Python Scripts", "*.py"),
                 ("Java Files", "*.java"), 
                 ("Html Files", "*.html;*.htm"),
                 ("CSS Files", "*.css"),
                 ("Amelitext Files", "*.amlt"),                 
                 ("JavaScript Files", "*.js"),
                 ("Batch Files", "*.bat")])
    if self.filename:
      self.textarea.delete(1.0, tk.END) #clears textarea 
      with open(self.filename, "r") as f:
        self.textarea.insert(1.0, f.read())
      self.set_window_title(self.filename)
    
  def save(self, *args):
    if self.filename:
      try:
        textarea_content = self.textarea.get(1.0, tk.END)
        with open(self.filename, "w") as f:
          f.write(textarea_content)
        self.statusbar.update_status(True)
      except Exception as e:
        print(e)
    else:
      self.save_as()
    
  def save_as(self, *args):
    try:
      new_file = filedialog.asksaveasfilename(
        initialfile="Untitled.txt",
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), 
                 ("Text Files", "*.txt"), 
                 ("Python Scripts", "*.py"),
                 ("Java Files", "*.java"), 
                 ("Html Files", "*.html;*.htm"),
                 ("CSS Files", "*.css"), 
                 ("Amelitext Files", "*.amlt"),
                 ("JavaScript Files", "*.js"),
                 ("Batch Files", "*.bat")])
      textarea_content = self.textarea.get(1.0, tk.END)
      with open(new_file, "w") as f:
        f.write(textarea_content)
      self.filename = new_file
      self.set_window_title(self.filename)
      self.statusbar.update_status(True)
    except Exception as e:
      print(e)

  def bind_shortcuts(self):
    self.textarea.bind('<Control-n>', self.new_file)
    self.textarea.bind('<Control-o>', self.open_file)
    self.textarea.bind('<Control-s>', self.save)    
    self.textarea.bind('<Control-S>', self.save_as)
    self.textarea.bind('<Key>', self.statusbar.update_status)
      
class Statusbar:

  def __init__(self, parent):
    font_specs3 = ("Alegreya Sans SC Light", 12)
    
    self.status = tk.StringVar()
    self.status.set("Amelietext  ⋯⋖✯✧✯⋗⋯  Version: 0.1")
    
    label = tk.Label(parent.textarea, textvariable=self.status, bg="#393838", bd=1, relief=tk.SUNKEN,
                     fg="#7FFFD4", anchor='sw', font=font_specs3)
    label.pack(side=tk.BOTTOM, fill=tk.BOTH)
    
  def update_status(self, *args):
    if isinstance(args[0], bool):
      self.status.set("Your file has been saved!")
    else:
      self.status.set("Amelietext  ⋯⋖✯✧✯⋗⋯  Version: 0.1")
      
 
if __name__ == "__main__":
  master = tk.Tk() #main part of text editor : text box
  amlt = Amelitext(master)
  master.mainloop()
  
