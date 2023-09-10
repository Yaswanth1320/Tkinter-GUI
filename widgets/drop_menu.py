from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Dropdown Menu")
root.geometry("400x400")

def display():
    label = Label(root, text=click.get()).pack()

option_list = [
    "Pizza", 
    "Burgur", 
    "fries", 
    "soft Drink",
    "coffee",
    "ice cream"
]

click = StringVar()
click.set(option_list[0])

drop = OptionMenu(root, click, *option_list)
drop.pack()

my_btn = Button(root, text="Select the item", command=display).pack()

root.mainloop()