from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Slider")
root.geometry('400x350')

v_slider = Scale(root, from_=0, to=350)
v_slider.pack()

h_slider = Scale(root, from_=0, to=400, orient=HORIZONTAL)
h_slider.pack()

my_label = Label(root, text=h_slider.get()).pack()

def h_slide():
    my_label = Label(root, text=h_slider.get()).pack() 
    root.geometry(str(h_slider.get())+'x'+str(v_slider.get()))

btn = Button(root, text="update", command=h_slide).pack()

root.mainloop()