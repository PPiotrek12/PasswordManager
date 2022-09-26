from Accounts import Accounts
from Encryption import Encryption
import values
from tkinter import *
from tkinter import messagebox

class AddAccount(Accounts):

    def addAccount(self):
        serviceName = self.service_name_entry.get()
        accLogin = self.login_entry.get()
        accPassword = self.password_entry.get()
        if serviceName in self.servicesList:
            Label(self.add_account_frame, text = "Such service exists.", fg = "red").grid(row = 6, column = 0)
            return

        enc = Encryption(values.key1, values.key2)
        encAccLogin = enc.encrypt(accLogin)
        encAccPassword = enc.encrypt(accPassword)

        newFile = open(values.data_path + serviceName + ".txt", 'w')
        print(encAccLogin, file = newFile)
        print(encAccPassword, file = newFile)
        newFile.close()

        servDataFile = open(values.data_path + "services.txt", 'a')
        print(serviceName, file = servDataFile)
        servDataFile.close()

        messagebox.showinfo(message = "New account has beed added successfully.")
        

    def __init__(self, root):
        super().__init__()
        self.root = root

        self.add_account_frame = Frame(root)
        self.add_account_frame.pack()

        self.service_name_entry = Entry(self.add_account_frame)
        self.login_entry = Entry(self.add_account_frame)
        self.password_entry = Entry(self.add_account_frame)
        btn = Button(self.add_account_frame, text = "Add", command = self.addAccount)

        Label(self.add_account_frame, text = "Insert service name", font = "Helvetica 20 bold").grid(row = 0, column = 0, pady = 20)
        self.service_name_entry.grid(row = 1, column = 0)
        Label(self.add_account_frame, text = "Insert your login", font = "Helvetica 18 bold").grid(row = 2, column = 0, pady = 20)
        self.login_entry.grid(row = 3, column = 0)
        Label(self.add_account_frame, text = "Insert your password", font = "Helvetica 18 bold").grid(row = 4, column = 0, pady = 20)
        self.password_entry.grid(row = 5, column = 0)
        btn.grid(row = 6, column = 0, pady = 20)
