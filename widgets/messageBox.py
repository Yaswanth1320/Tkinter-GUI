from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("MessageBox")

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response= messagebox.askyesno("This is my popup", "Hello World")
    if response == 1:
        Label(root, text="yes button is clicked").pack()
    else:
        Label(root,text ="No Button Clicked ").pack()


button = Button(root, text="popup", command=popup).pack()

root.mainloop()