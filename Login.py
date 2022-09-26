from tkinter import *
import hashlib
import values
from Get_keys import Get_keys

class Login:
    def check(self):
        password = self.entry.get()
        hash = hashlib.new('sha256')
        hash.update(password.encode())
        if self.fileHash != hash.hexdigest():
            Label(self.login_frame, text = "Wrong password, try again.", fg = "red").grid(row = 3, column = 0, pady = 10)
        else:
            self.login_frame.pack_forget()
            get_keys = Get_keys(self.root)

    def __init__(self, root):
        self.root = root
        file = open(values.data_path + "login.txt", 'r')
        self.fileHash = file.readline()
        self.fileHash = self.fileHash[:len(self.fileHash)-1]
        file.close()

        self.login_frame = Frame(self.root)
        self.login_frame.pack()
        self.entry = Entry(self.login_frame, width = 35)
        btn = Button(self.login_frame, text = "Login", command = self.check)

        Label(self.login_frame, text = "Insert your password.", font = "Helvetica 25 bold").grid(row = 0, column = 0, pady = 20)
        self.entry.grid(row = 1, column = 0, pady = 10)
        btn.grid(row = 2, column = 0, pady = 10)
