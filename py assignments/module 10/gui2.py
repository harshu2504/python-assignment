from tkinter import *
from tkinter import messagebox


window=Tk()
window.title("Python application")
def GUI_Tutorial():
   # Label(window,text="GUI with Tkinter").grid()
    messagebox.showinfo("alert box","You clicked on button")

a="C:\\Users\\adichouhanofficial\\Pictures\\ganesh.png"
icon = PhotoImage(file=a)
l1=Label(window,image=icon).pack()
#Button(window,text="Click Me", command= GUI_Tutorial).pack()
window.mainloop()
