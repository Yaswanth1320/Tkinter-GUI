from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Frames")

# frame = LabelFrame(root, text="This id the frame.....", padx=5, pady=5)
# frame.pack(padx=10, pady=10)

# button = Button(frame, text="Click me")
# button.pack()
r = IntVar()
r.set("2")

Radiobutton(root, text="Option 1",variable=r, value=1).pack()
Radiobutton(root, text="Option 1",variable=r, value=2).pack()

mylabel = Label(root, text=r.get())
mylabel.pack()

root.mainloop()

