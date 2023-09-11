import tkinter
import pyshorteners

root = tkinter.Tk()
root.title("Url Shortener")
root.geometry("350x150")

def Shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(originalUrl_entry.get())
    shortenUrl_entry.insert(0, short_url)

originalUrl_label = tkinter.Label(root, text="Enter the Long Url")
originalUrl_entry = tkinter.Entry(root)
shortenUrl_label = tkinter.Label(root, text="Shortend Url")
shortenUrl_entry = tkinter.Entry(root)
convert = tkinter.Button(root, text="convert",command=Shorten)

originalUrl_label.pack()
originalUrl_entry.pack()
shortenUrl_label.pack()
shortenUrl_entry.pack()
convert.pack()

root.mainloop()