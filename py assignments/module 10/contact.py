from tkinter import *
window=Tk()
window.title("Contact application")
window.geometry('400x400')
top_frame = Frame(window).pack()
Label(top_frame,text="Contact Details").pack()

Label(window,text="Rno").grid(row=2,column=0)
Label(window,text="Name").grid(row=4,column=0)
Label(window,text="Phone").grid(row=6,column=0)
Label(window,text="Contact").grid(row=8,column=0)
Entry(window).grid(row=2,column=1)
Entry(window).grid(row=4,column=1)
Entry(window).grid(row=6,column=1)
Entry(window).grid(row=8,column=1)
window.mainloop()