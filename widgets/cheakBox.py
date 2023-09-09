from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("CheakBox")
root.geometry('400x400')

def update():
    my_label = Label(root, text=var.get()).pack()

var = IntVar()

cb =Checkbutton(root, text="click here", variable=var).pack()
my_btn = Button(root, text="update", command=update).pack()

root.mainloop()


