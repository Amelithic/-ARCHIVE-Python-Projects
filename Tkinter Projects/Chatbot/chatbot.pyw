# simple chatoo boota
# by Amelithic
# 24/5 April 2020

import tkinter as tk
import time
import os
import random
from datetime import datetime
from dotenv import load_dotenv
from tkinter import messagebox
import keyboard as kbd

env_path = '.env' #explicitly providing path to '.env'
load_dotenv(dotenv_path=env_path)

HELLO_IN = os.getenv('HELLO_INPUT')
BYE_IN = os.getenv('BYE_INPUT')
GOOD_IN = os.getenv('GOOD_INPUT')
BAD_IN = os.getenv('BAD_INPUT')
HOW_ARE_IN = os.getenv('HOW_INPUT')

author = 'Amelithic' #creator of chatbot


def prontus():
    print('WWWAAAOOOOWWWWHH')
    

def make_username(): 
    print('Username is: ' + username.get())
    name_set['text'] = 'Saved!'

def lezgo():
    window1.destroy()
    
    window2 = tk.Tk()
    window2.title('Chatbot')
    window2.geometry('580x480')
    window2.configure(bg="#151414")
    
    lab1 = tk.Label(window2, font=("Abel", 12), bg="#151414", fg="white", text="AMELIEBOT (chatbot V.1)") 
    lab1.pack()
    lab2 = tk.Label(window2, font=("Abel", 14), bg="#151414", fg="white", text="=======================") 
    lab2.pack()
    
    messages = tk.Text(window2, bg="#070707", fg="white")
    messages.configure(state='disabled')
    messages.pack()
    #scrolb = tk.Scrollbar(window2, command=messages.yview)

    input_user = tk.StringVar()
    input_field = tk.Entry(window2, text=input_user, bg="#252525", fg="white", font=("Abel", 14), bd=1)
    input_field.pack(side=tk.BOTTOM, fill=tk.X)
    
    bot_name = "Bob the Bot"
    bot_prefix = ('<' + bot_name + '> ')
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    def Enter_pressed(event):
        messages.configure(state='normal')
        input_get = input_field.get()
        print("<" + str(username.get()) + "> " + input_get)
        messages.insert(tk.INSERT, "<" + str(username.get()) + "> " + '%s\n' % input_get)

        if input_get.casefold() in HELLO_IN.casefold():
            hello_outt = [(bot_prefix + 'Hello ' + username.get() + ', how are you?'), (bot_prefix + 'Hey ' + username.get() + ', how are you doing?')]
            hello_out = random.choice(hello_outt)
            print(hello_out)
            messages.insert(tk.INSERT, hello_out + '\n')
        elif input_get.casefold() in GOOD_IN.casefold():
            good_outt = [(bot_prefix + 'That\'s great!'), (bot_prefix + 'Yes, ' + input_get + ' indeed!')]
            good_out = random.choice(good_outt)
            print(good_out)
            messages.insert(tk.INSERT, good_out + '\n')
        elif input_get.casefold() in BAD_IN.casefold():
            bad_out = (bot_prefix + 'That\'s a shame! Hope you feel better soon!')
            print(bad_out)
            messages.insert(tk.INSERT, bad_out + '\n')    
        elif input_get == 'what time is it?':
            time_out = (bot_prefix + 'It is: ' + current_time)
            print(time_out)
            messages.insert(tk.INSERT, time_out + '\n')
        elif input_get.casefold() in HOW_ARE_IN.casefold():
            how_out = (bot_prefix + 'I can\'t feel emotions... but probably pretty good!')
            print(how_out)
            messages.insert(tk.INSERT, how_out + '\n')
        elif input_get == 'who are you?':
            who_outt = [(bot_prefix + 'I\'m ' + bot_name + ' but you can call me BBB for short ;) '), (bot_prefix + 'I am ' + bot_name + ', an intelligent chatbot by ' + author + '!')]
            who_out = random.choice(who_outt)
            print(who_out)
            messages.insert(tk.INSERT, who_out + '\n')
        elif input_get.casefold() in BYE_IN.casefold():
            bye_out = (bot_prefix + 'Bye ' + username.get() + '!')
            print(bye_out)
            messages.insert(tk.INSERT, bye_out + '\n')

        input_user.set('')
        time.sleep(0.5)
        messages.configure(state='disabled')
        time.sleep(0.1)
        messages.see("end")
        return "break"


    def show_save_menu():
        filename = 'log.txt'
        messagelog = messages.get('1.0', tk.END)
        save_text = open(filename, 'a') #a = append (write to end of file) >>> this is the mode of open(file) <<< can replace with 'w' or 'r'
        
        print('Opened save menu.')
        box_title = "Save conversation"
        box_message = "Save your current conversation to a *.txt file?"
        MsgBox = tk.messagebox.askquestion(box_title, box_message)
        if MsgBox == 'yes':
            print('Saved to *.txt file!')
            save_text.write('{' + str(now) + '} \n' + messagelog + '\n')
            save_text.close()
        else:
            print('Exited save menu.')
    kbd.add_hotkey('ctrl + s', show_save_menu)
    
    frame = tk.Frame(window2)  # , width=300, height=300)
    input_field.bind("<Return>", Enter_pressed)
    frame.pack()
    
    #print(str(input_field.get()))
    #print(str(input_user.get()))

    window2.mainloop()
    

window1 = tk.Tk()
window1.title('Chatbot >> Start')
#window1.geometry('500x500')
window1.configure(bg="#151414")

    
label1 = tk.Label(window1, font=("Abel", 12), bg="#151414", fg="white", text="AMELIEBOT (chatbot V.1)") 
label1.pack()
label2 = tk.Label(window1, font=("Abel", 14), bg="#151414", fg="white", text="=======================") 
label2.pack()

label22 = tk.Label(window1, font=("System", 12), bg="#151414", fg="white", text="<< USERNAME:  >>") 
label22.pack()

username = tk.StringVar()
in_name = tk.Entry(window1, textvariable=username, bg="#252525", fg="white", font=("Abel", 14))
in_name.pack()

#s = "<" + str(username.get()) + "> "
#s = username.get()
    
name_set = tk.Button(window1, bg="#252424", fg="white", text="Save name", font=("system", 14), command=make_username)
name_set.pack()
label24 = tk.Label(window1, font=("Abel", 14), bg="#151414", fg="white", text="=======================") 
label24.pack()


button_widget = tk.Button(window1, bg="#252424", fg="white", text="Get started?", font=("system", 20), command=lezgo)
button_widget.pack()
label3 = tk.Label(window1, font=("Abel", 14), bg="#151414", fg="white", text="=======================")
label3.pack()


window1.mainloop()