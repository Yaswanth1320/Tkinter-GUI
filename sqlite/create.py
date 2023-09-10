from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Database Creation")
root.geometry("400x400")

#Creating a database
conn = sqlite3.connect("book.db")

#Create a cursor
cursor = conn.cursor()

#Creating a table
conn.execute("""CREATE TABLE book_table(
             name text,
             author text,
             zipcode integer,
             price integer)
             """)


#commit changes
conn.commit()

#Close connection
conn.close()

root.mainloop()