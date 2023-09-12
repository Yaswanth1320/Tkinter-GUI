import tkinter 
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk

root = tkinter.Tk()
root.geometry("1000x600")
root.title("Image Editor Tool")
root.config(bg="white")

pen_color = "black"
pen_size = 5
filepath = ""

def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Choose Pen Color")[1]


def change_size(size):
    global pen_size
    pen_size = size

def clear_canvas():
    canvas.delete("all")
    canvas.create_image(0, 0, image=canvas.image, anchor="nw")

def draw(event):
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')

def apply_filter(filter):
    image = Image.open(filename)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.ANTIALIAS)
    if filter == "Black and White":
        image = ImageOps.grayscale(image)
    elif filter == "Blur":
        image = image.filter(ImageFilter.BLUR)
    elif filter == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    elif filter == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)
    elif filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)
    elif filter == "Original":
        pass
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")

def add_image():
    global filename
    filename = filedialog.askopenfilename(initialdir="/Users/yaswanth/Python:Tkinter/projects")

    image = Image.open(filename)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.ANTIALIAS)
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw") 
    

top_frame = tkinter.Frame(root, width=1000, height=100, bg="white") 
top_frame.pack(side="top", fill="x")

canvas = tkinter.Canvas(root, width=1000, height=500)
canvas.pack()

img_button = tkinter.Button(top_frame, text="Add Image",command=add_image, bg="white")
img_button.grid(row=0, column=2, padx=20)

color_btn = tkinter.Button(top_frame, text="Choose pen color", command=change_color, bg="white")
color_btn.grid(row=0, column=1, padx=20)


pen_size_frame = tkinter.Frame(top_frame, bg="white")
pen_size_frame.grid(row=0,column=0, padx=40)

label = tkinter.Label(pen_size_frame, text="Select the pen size", bg="white")
label.pack()

small = tkinter.Radiobutton(pen_size_frame, text="Small", value=3, command=lambda: change_size(3), bg="white")
small.pack()

medium = tkinter.Radiobutton(pen_size_frame, text="Medium", value=5, command=lambda: change_size(5), bg="white")
medium.pack()
medium.select()

large = tkinter.Radiobutton(pen_size_frame, text="Large", value=7, command=lambda: change_size(7), bg="white")
large.pack()

clear_button = tkinter.Button(top_frame, text="Clear",command=clear_canvas)
clear_button.grid(row=0, column=3, padx=20)

fliter_frame = tkinter.Frame(top_frame, bg="white")
fliter_frame.grid(row=0, column=4 ,padx=20)

filter_label = tkinter.Label(fliter_frame, text="Choose Filter", background="white")
filter_label.pack()
filter_combobox = ttk.Combobox(fliter_frame, values=["Black and White", "Blur", "Emboss", "Sharpen", "Smooth", "Original"])
filter_combobox.pack()

filter_combobox.bind("<<ComboboxSelected>>",lambda event: apply_filter(filter_combobox.get()))






canvas.bind("<B1-Motion>", draw)

root.mainloop()