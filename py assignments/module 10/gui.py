'''import tkinter

# 3 d/f layout 1.pack , 2. grid 3. pad
window = tkinter.Tk()
window.title("GUI")
window.geometry('400x400')
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side="bottom")
label = tkinter.Label(window,text="Welcome to GUI's Tutorial on Tkinter").pack()
btn1 = tkinter.Button(top_frame, text="Button1", fg="red", bg="green").pack()
btn2 = tkinter.Button(top_frame, text="Button2", fg="yellow", bg="cyan").pack()

window.mainloop()
'''

from tkinter import *
window = Tk()
window.geometry('400x400')
checkVar1 = IntVar()
checkVar2 = IntVar()
name = Label(window,text="Name").grid(row=0,column=0)
password = Label(window,text="Password").grid(row=3,column=0)
Checkbutton(window, text="Machine Learning",variable=checkVar1,onvalue=1,offvalue=0).grid(row=10,sticky=N,column=0)
Checkbutton(window, text="Deep Learning",variable=checkVar2,onvalue=1,offvalue=0).grid(row=13,sticky=N,column=0)

Entry(window).grid(row=0,column=1)
Entry(window).grid(row=3,column=1)
top.mainloop()
