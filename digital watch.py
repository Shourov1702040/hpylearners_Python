# Delta electro code
# Md Touhid Islam
# https://www.facebook.com/shourov40


from tkinter import *
from time import strftime

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

root = Tk()

label = Label(root,font = "Digital-7 25 bold",fg='green')
label.pack(pady=20)
time()

root.geometry('300x120+400+300')
root.mainloop()
