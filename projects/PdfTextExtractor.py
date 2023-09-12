import tkinter
import PyPDF2
from tkinter import filedialog

def openfile():
    filename = filedialog.askopenfilename(title="Open Pdf file",
                                          initialdir="/Users/yaswanth/Python:Tkinter/projects/files",
                                          filetypes=[('Pdf files', '*.pdf')])
    
    filename_label.configure(text=filename)
    extractor_text.delete("1.0", tkinter.END)
    reader = PyPDF2.PdfReader(filename)
    for i in range(reader.numPages):
            current_text = reader.getPage(i).extractText()
            extractor_text.insert(tkinter.END, current_text)

root = tkinter.Tk()
root.title("Pdf Text Extractor")

filename_label = tkinter.Label(root, text="No file Selected")
extractor_text = tkinter.Text(root)
openfile_button = tkinter.Button(root ,text ="Open File", command=openfile)

filename_label.pack()
extractor_text.pack()
openfile_button.pack()

root.mainloop()