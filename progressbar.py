# Delta electro code
# Md Touhid Islam
# https://www.facebook.com/shourov40


from tkinter import *
from tkinter.ttk import *

def bar():
    import time
    for i in range(1,101,1):
        progress['value'] = i
        root.update_idletasks()
        lb.config(text=str(i)+"%")
        time.sleep(0.03)

    progress['value'] = 100
    root.destroy()


root = Tk()

f1 = "arial 15 bold"
lb = Label(root,text="",font=f1)
lb.pack(padx=80)

s = Style()
s.configure("TProgressbar", foreground='#09BF14', background='#09BF14', thickness=100)

progress = Progressbar(root,style="TProgressbar", length=700, mode='determinate')
progress.pack(pady=10,padx=5)

btn = Button(root, text='Start', command=bar)
btn.pack(pady=10)

root.geometry("710x150+200+200")
root.title("progress")
mainloop()
