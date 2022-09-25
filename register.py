import hashlib
import values
from tkinter import *
from login import login
from tkinter import messagebox

def savePassword(root, frame, entry1, entry2):
    password1 = entry1.get()
    password2 = entry2.get()
    if password1 != password2:
        Label(frame, text = "Paswwords doesn't match.").grid(row = 5, column = 0)
    else:
        hash = hashlib.new('sha256')
        hash.update(password1.encode())
        file = open(values.data_path + "login.txt", 'w')
        print(hash.hexdigest(), file=file)
        file.close()
        messagebox.showinfo(message = "You are registered, can log in now.")
        frame.pack_forget()
        login(root)

def register(root):
    registration_frame = Frame(root)
    registration_frame.pack()

    Label(registration_frame, text = "Insert your new password.").grid(row = 0, column = 0)
    entry1 = Entry(registration_frame)
    entry1.grid(row = 1, column = 0)

    Label(registration_frame, text = "Confirm your new password.").grid(row = 2, column = 0)
    entry2 = Entry(registration_frame)
    entry2.grid(row = 3, column = 0)

    btn = Button(registration_frame, text = "Register", command = lambda: savePassword(root, registration_frame, entry1, entry2))
    btn.grid(row = 4, column = 0)
