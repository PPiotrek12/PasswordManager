import hashlib
import values
from tkinter import *
from Login import Login
from tkinter import messagebox

class Register():

    def savePassword(self):
        password1 = self.entry1.get()
        password2 = self.entry2.get()
        if password1 != password2:
            Label(self.registration_frame, text = "Paswwords doesn't match, try again.", fg = "red").grid(row = 5, column = 0, pady = 10)
        else:
            hash = hashlib.new('sha256')
            hash.update(password1.encode())
            file = open(values.data_path + "login.txt", 'w')
            print(hash.hexdigest(), file=file)
            file.close()
            messagebox.showinfo(message = "You are registered, can log in now.")
            self.registration_frame.pack_forget()
            login = Login(self.root)

    def __init__(self, root):
        self.root = root
        self.registration_frame = Frame(self.root)
        self.registration_frame.pack()

        self.entry1 = Entry(self.registration_frame)
        self.entry2 = Entry(self.registration_frame)
        btn = Button(self.registration_frame, text = "Register", command = self.savePassword)

        Label(self.registration_frame, text = "Insert your new password.", font = "Helvetica 25 bold").grid(row = 0, column = 0, pady = 20)
        self.entry1.grid(row = 1, column = 0)
        Label(self.registration_frame, text = "Confirm your new password.", font = "Helvetica 23 bold").grid(row = 2, column = 0, pady = 20)
        self.entry2.grid(row = 3, column = 0)
        btn.grid(row = 4, column = 0, pady = 10)
