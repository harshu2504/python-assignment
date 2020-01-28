from tkinter import *


def btn_click(item):
    global expression
    expression+= str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression=""
    input_text.set("")

def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression=""
expression=""
input_text = StringVar()
input_frame = Frame(window,width=312, height =50, bd=0)
input_frame.pack(side =TOP)






window=Tk()


window.mainloop()
