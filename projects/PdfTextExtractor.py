import tkinter
import pyPDf2
from tkinter import filedialog


def openfile():
    filename = filedialog.askopenfilename(title="Open Pdf file",
                                          initialdir="/Users/yaswanth/Python:Tkinter/projects",
                                          filetypes=[('Pdf files', '*.pdf')])

root = tkinter.Tk()
root.title("Pdf Text Extractor")

filename_label = tkinter.Label(root, text="No file Selected")
extractor_text = tkinter.Text(root)
openfile_button = tkinter.Button(root ,text ="Open File", command=openfile)

filename_label.pack()
extractor_text.pack()
openfile_button.pack()

root.mainloop()