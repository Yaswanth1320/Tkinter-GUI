from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image slider")
root.iconbitmap('icon.ico')

my_image1 = ImageTk.PhotoImage(Image.open('./images/luffy.jpeg'))
my_image2 = ImageTk.PhotoImage(Image.open('./images/zoro.jpg'))
my_image3 = ImageTk.PhotoImage(Image.open('./images/sanji.jpeg'))

image_list = [my_image1, my_image2, my_image3]

status = Label(root, text=" Image 1 0f "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


my_label = Label(image=my_image1)
my_label.grid(row=0,column=0, columnspan=3)

def forward(image_no):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label = Label(image= image_list[image_no - 1])
    button_forward = Button(root, text=">>", command=lambda : forward(image_no + 1))
    button_back = Button(root, text="<<", command= lambda : backward(image_no -1))
    if image_no == 3:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text=" Image " + str(image_no) +" 0f "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    
def backward(image_no):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label.grid_forget()
    my_label = Label(image= image_list[image_no - 1])
    button_forward = Button(root, text=">>", command=lambda : forward(image_no + 1))
    button_back = Button(root, text="<<", command= lambda : backward(image_no -1))

    if image_no == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text=" Image " + str(image_no) +" 0f "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", command= backward, state=DISABLED)
button_exit = Button(root, text="EXIT", command=root.quit)
button_forward = Button(root, text=">>", command=lambda : forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()