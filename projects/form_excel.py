import tkinter
from tkinter import ttk
import os
import openpyxl

def fill_data():
    accept = accept_var.get()

    if accept == "Accepted":
        firstname = first_name_entry.get()
        lastname  = last_name_entry.get()
        title = surname_entry.get()
        Nationality =nationality_entry.get()
        age = age_entry.get()

        resgistration = regi_var.get()
        numcourses = num_of_courses_entry.get()
        numsemesters = num_of_courses_entry.get()

        print("First Name :", firstname, "Last Name : ", lastname)
        print("Surname :", title, "Nationality : ", Nationality)
        print("Age :", age, "Registration : ", resgistration)
        print("Courses :", numcourses, "Semesters : ", numsemesters)
        print("---------------------------------------------------------------")

        path ="/Users/yaswanth/Python:Tkinter/data.xlsx"

        if not os.path.exists(path):
            excel = openpyxl.Workbook()
            sheet = excel.active
            headings = ["First Name" ,"Last Name", "Surname", "Nationality", "Age", "Registration","No of Courses", "No of semesters"]
            sheet.append(headings)
            excel.save(path)

        excel = openpyxl.load_workbook(path)
        sheet = excel.active
        sheet.append([firstname,lastname,title,Nationality,age,resgistration,numcourses,numsemesters])
        excel.save(path)

        root.destroy()


    else:
        label = tkinter.Label(window, text="please Cheack in  the terms and conditions before submiting", bg="red")
        label.grid(row=4, column=0)
        # print("Cheack the terms and conditions")


root = tkinter.Tk()
root.title("Entry Form")

window = tkinter.Frame(root)
window.pack()

user_frame = tkinter.LabelFrame(window, text="User Information")
user_frame.grid(row=0, column=0, padx=20, pady=10)

first_name = tkinter.Label(user_frame, text="First Name")
first_name.grid(row=0, column=0)
last_name = tkinter.Label(user_frame, text="Last Name")
last_name.grid(row=0,column=1)

first_name_entry = tkinter.Entry(user_frame)
last_name_entry = tkinter.Entry(user_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

surname = tkinter.Label(user_frame, text="Surname")
surname.grid(row=0, column=3)
surname_entry = ttk.Combobox(user_frame, values=["", "Mr.", "Ms.", "Dr."])
surname_entry.grid(row=1, column=3)

age_label = tkinter.Label(user_frame, text="Age")
age_entry = tkinter.Spinbox(user_frame, from_=10, to=100)
age_label.grid(row=2, column=0)
age_entry.grid(row=3, column=0)

nationality = tkinter.Label(user_frame, text="Nationality")
nationality_entry = ttk.Combobox(user_frame, values=["India", "America", "Africa", "Europe", "Asia", "Austrila"])
nationality.grid(row=2,column=1)
nationality_entry.grid(row=3, column=1)

for widget in user_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

Course_frame = tkinter.LabelFrame(window, text="Course Information")
Course_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

regi_var = tkinter.StringVar(value="Not registred")
resgistration = tkinter.Label(Course_frame, text="Registration Status")
resgistration_cheak = tkinter.Checkbutton(Course_frame, text="Currently Registered", variable=regi_var, onvalue="Registred", offvalue="Not registred")
resgistration.grid(row=0, column=0)
resgistration_cheak.grid(row=1, column=0)

num_of_courses = tkinter.Label(Course_frame, text="# Courses Completed")
num_of_courses_entry = ttk.Spinbox(Course_frame, from_=0, to=27)
num_of_courses.grid(row=0, column=1)
num_of_courses_entry.grid(row=1, column=1)

num_of_semesters = tkinter.Label(Course_frame, text="# Semesters")
num_of_semesters_entry = ttk.Spinbox(Course_frame, from_=0, to="infinity")
num_of_semesters.grid(row=0, column=2)
num_of_semesters_entry.grid(row=1, column=2)

for widget in Course_frame.winfo_children():
    widget.grid_configure(padx=20, pady=5)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_frame = tkinter.LabelFrame(window, text="Terms & conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)
term_check = tkinter.Checkbutton(terms_frame, text=" I accept the terms and conditions", variable=accept_var, onvalue= "Accepted", offvalue="Not Accepted")
term_check.grid(row=0, column=0)

button = tkinter.Button(window, text="Enter Data", command=fill_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

root.mainloop()