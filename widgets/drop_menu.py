from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Dropdown Menu")
root.geometry("400x400")

click = StringVar()
click.set("Pizza")

drop = OptionMenu(root, click, "Pizza", "Burgur", "fries", "soft Drink")
drop.pack()

root.mainloop()