from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Database Creation")
root.geometry("400x400")

#Creating a table
# conn.execute("""CREATE TABLE book(
#              name text,
#              author text,
#              zipcode integer,
#              price integer)
#              """)

#creating submit function

def submit():
    #Creating a database
    conn = sqlite3.connect("book.db")

    #Create a cursor
    cursor = conn.cursor() 

    #Insert into table
    conn.execute("INSERT INTO book_table VALUES(:name, :author, :zipcode, :price)",
                 {
                  'name' : name.get(),
                  'author' : author.get(),
                  'zipcode' : zipcode.get(),
                  'price' : price.get()  
                 }
                 )
    
    #commit changes
    conn.commit()

    #Close connection
    conn.close()

    name.delete(0,END)
    author.delete(0,END)
    zipcode.delete(0,END)
    price.delete(0,END)

    

#Creating text boxes
name = Entry(root, width=30)
name.grid(row=0, column=1, padx=20)
author = Entry(root, width=30)
author.grid(row=1, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=2, column=1)
price = Entry(root, width=30)
price.grid(row=3, column=1)

#Creating labels for text boxes
name_label = Label(root, text="name")
name_label.grid(row=0, column=0)
author_label = Label(root, text="author")
author_label.grid(row=1, column=0)
zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row=2, column=0)
price_label = Label(root, text="price")
price_label.grid(row=3, column=0)

#Submit button
submit = Button(root, text="Insert data", command=submit)
submit.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


root.mainloop()