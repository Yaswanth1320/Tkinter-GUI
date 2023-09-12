import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title("Login Form")
root.geometry("340x440")
root.configure(bg="#333333")

def login():
    username_list = ["yaswanth1320", "john123", "harry2023"]
    password_list = ["yaswanth@123", "1234", "1320"]
    for i,j in zip(username_list,password_list):

        if username_entry.get() == i and password_entry.get()==j :
            messagebox.showinfo(title="Login Success", message="You successfully logged in")
            root.destroy()
            return
            
    messagebox.showinfo(title="Login Failed", message="Invalid Login")    

frame = tkinter.Frame(root, bg="#333333")

username_label = tkinter.Label(frame, text="Username :", bg="#333333", fg="#FFFFFF", font=('Calibri, 16'))
username_entry = tkinter.Entry(frame, font=('Calibri, 16'))
password_label = tkinter.Label(frame, text="Password :", bg="#333333", fg="#FFFFFF",  font=('Calibri, 16'))
password_entry = tkinter.Entry(frame, show="*",  font=('Calibri, 16'))
login_label = tkinter.Label(frame, text="Login", bg="#333333", fg="#FFFFFF",font=('Calibri, 25'))
login_button = tkinter.Button(frame, text="Log In",font=('Calibri, 16'), command=login)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=10, padx=5)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=10, padx=5)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

root.mainloop()