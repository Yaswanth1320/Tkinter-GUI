from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Dialog Box")

def open():
    global my_image
    root.file = filedialog.askopenfilename(initialdir="./images", title="Select a file",filetypes=(("png files" , "*.png"),("all files" , "*.*")))
    my_image = ImageTk.PhotoImage(Image.open(root.file))
    my_image_label = Label(image=my_image).pack()


btn =Button(root, text="Open file", command=open).pack()

root.mainloop()