import customtkinter as ctk

def add_work():
    work = entry.get()
    label = ctk.CTkLabel(scroll_frame, text=work)
    label.pack()
    entry.delete(0, ctk.END)

root = ctk.CTk()
root.geometry("800x500")
root.title("Todo App")

title_label = ctk.CTkLabel(root, text="Daily Tasks", font=ctk.CTkFont(size=30))
title_label.pack(padx=10, pady=(40, 20))

scroll_frame = ctk.CTkScrollableFrame(root, width=500, height=200)
scroll_frame.pack()

entry = ctk.CTkEntry(scroll_frame, placeholder_text="Add todo")
entry.pack(fill="x")

add_button = ctk.CTkButton(root, text="Add", width=500, command=add_work)
add_button.pack(pady=20)

root.mainloop()