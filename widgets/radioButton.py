from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("RadioButton")

TOPPINGS= [
    ("classic","classic"),
    ("chicken","chicken"),
    ("panneer","panneer"),
    ("mushroom","mushroom"),
    ("onion","onion"),
]

pizza = StringVar()
pizza.set("classic")

for text,toppings in TOPPINGS:
    Radiobutton(root, text=text ,variable=pizza, value=toppings).pack()

def clicked(value):
    mylabel = Label(root, text=value)
    mylabel.pack()



button = Button(root, text="ADD TOPPINGS" ,command=lambda :clicked(pizza.get()))
button.pack()



root.mainloop()

