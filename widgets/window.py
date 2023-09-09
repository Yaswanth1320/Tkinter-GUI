from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Main Window")

def open():
    global my_image
    new = Toplevel()
    new.title("New Window")
    my_image = ImageTk.PhotoImage(Image.open("./images/world.png"))
    label = Label(new, image=my_image).pack()
    btn =Button(new, text="Exit window", command=new.destroy).pack()
    
button = Button(root, text="Open new window", command=open).pack()





root.mainloop()