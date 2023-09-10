from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Database Creation")
root.geometry("400x500")

#Creating a table
# conn.execute("""CREATE TABLE book(
#              name text,
#              author text,
#              zipcode integer,
#              price integer)
#              """)

#Function to delete a record

def change():
    #Creating a database
    conn = sqlite3.connect("book.db")

    #Create a cursor
    cursor = conn.cursor() 

    record_id = delete_box.get()
    cursor.execute("""UPDATE book_table SET
                   name = :name,
                   author = :author,
                   zipcode = :zipcode,
                   price = :price

                   WHERE oid = :oid """,
                    {
                    'name' : name_editor.get(),
                  'author' : author_editor.get(),
                  'zipcode' : zipcode_editor.get(),
                  'price' : price_editor.get(),
                  'oid' : record_id
                    
                    })    

    #commit changes
    conn.commit()

    #Close connection
    conn.close()

    update.destroy()

    

def  edit():
    global update
    update = Tk()
    update.title("Updating a record")
    update.geometry("400x200")
    #Creating text boxes]

    #Creating a database
    conn = sqlite3.connect("book.db")

    #Create a cursor
    cursor = conn.cursor() 

    #query to fetech data
    record_id = delete_box.get()
    cursor.execute("SELECT * FROM book_table WHERE oid = " + record_id)
    records = cursor.fetchall()


    global name_editor
    global author_editor
    global zipcode_editor
    global price_editor

    name_editor = Entry(update, width=30)
    name_editor.grid(row=0, column=1, padx=20)
    author_editor = Entry(update, width=30)
    author_editor.grid(row=1, column=1)
    zipcode_editor = Entry(update, width=30)
    zipcode_editor.grid(row=2, column=1)
    price_editor = Entry(update, width=30)
    price_editor.grid(row=3, column=1)


    #Creating labels for text boxes
    name_label = Label(update, text="name")
    name_label.grid(row=0, column=0)
    author_label = Label(update, text="author")
    author_label.grid(row=1, column=0)
    zipcode_label = Label(update, text="zipcode")
    zipcode_label.grid(row=2, column=0)
    price_label = Label(update, text="price")
    price_label.grid(row=3, column=0)

    for record in records:
        name_editor.insert(0,record[0])
        author_editor.insert(0,record[1])
        zipcode_editor.insert(0,record[2])
        price_editor.insert(0,record[3])

    update_records = Button(update, text="Save record", command=change)
    update_records.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=87)
    

#Function to delete a record
def delete():
    #Creating a database
    conn = sqlite3.connect("book.db")

    #Create a cursor
    cursor = conn.cursor()

    #query for deleting command
    cursor.execute("DELETE from book_table WHERE oid= " + delete_box.get())

    #commit changes
    conn.commit()

    #Close connection
    conn.close()
    

def submit():
    #Creating a database
    conn = sqlite3.connect("book.db")

    #Create a cursor
    cursor = conn.cursor() 

    #Insert into table
    cursor.execute("INSERT INTO book_table VALUES(:name, :author, :zipcode, :price)",
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

#creating display function

def display():
    #Creating a database
    conn = sqlite3.connect("book.db")

    #Create a cursor
    cursor = conn.cursor() 

    #query to fetech data
    cursor.execute("SELECT *,oid FROM book_table")
    records = cursor.fetchall()
    
    print_record = ''
    for record in records:
        print_record += str(record) + "\n"

    record_label = Label(root, text=print_record)
    record_label.grid(row=10, column=0, columnspan=2)

    #commit changes
    conn.commit()

    #Close connection
    conn.close()




#Creating text boxes
name = Entry(root, width=30)
name.grid(row=0, column=1, padx=20)
author = Entry(root, width=30)
author.grid(row=1, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=2, column=1)
price = Entry(root, width=30)
price.grid(row=3, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=6,column=1)


#Creating labels for text boxes
name_label = Label(root, text="name")
name_label.grid(row=0, column=0)
author_label = Label(root, text="author")
author_label.grid(row=1, column=0)
zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row=2, column=0)
price_label = Label(root, text="price")
price_label.grid(row=3, column=0)

delete_label = Label(root, text="select ID")
delete_label.grid(row=6, column=0)

#Submit button
submit = Button(root, text="Insert data", command=submit)
submit.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Button to display records


show_records = Button(root, text="show records", command=display)
show_records.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=92)

delete_records = Button(root, text="Delete records", command=delete)
delete_records.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=87)

update_records = Button(root, text="Update records", command=edit)
update_records.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=87)

root.mainloop()