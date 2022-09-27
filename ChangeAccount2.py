from Accounts import Accounts
from tkinter import *
from Encryption import Encryption
from tkinter import messagebox
import values

class ChangeAccount2(Accounts):
    def back_to_change(self):
        self.change_account_frame2.pack_forget()
        self.change_account_frame.pack()

    def changeAccount2(self):
        accLogin = self.login_entry.get()
        accPassword = self.password_entry.get()

        enc = Encryption(values.key1, values.key2)
        encAccLogin = enc.encrypt(accLogin)
        encAccPassword = enc.encrypt(accPassword)

        newFile = open(values.data_path + self.serviceName + ".txt", 'w')
        print(encAccLogin, file = newFile)
        print(encAccPassword, file = newFile)
        newFile.close()

        messagebox.showinfo(message = "You have successfully changed account's data.")
        self.back_to_change()

    def __init__(self, root, change_account_frame, number):
        super().__init__()
        self.root = root
        self.change_account_frame = change_account_frame
        self.change_account_frame2 = Frame(self.root)
        self.change_account_frame2.pack()
        self.number = number
        self.serviceName = self.servicesList[number]

        self.login_entry = Entry(self.change_account_frame2)
        self.password_entry = Entry(self.change_account_frame2)
        btn = Button(self.change_account_frame2, text = "Change", command = self.changeAccount2, width = 15)
        btnBack = Button(self.change_account_frame2, text = "Back", command = self.back_to_change, width = 15)

        Label(self.change_account_frame2, 
            text = f"Changing {self.serviceName} account's data.", font = "Helvetica 20 bold").grid(row = 0, column = 0, pady = 30)
        Label(self.change_account_frame2, text = "Insert new login", font = "Helvetica 13 bold").grid(row = 1, column = 0)
        self.login_entry.grid(row = 2, column = 0, pady = 20)
        Label(self.change_account_frame2, text = "Insert new password", font = "Helvetica 12 bold").grid(row = 3, column = 0)
        self.password_entry.grid(row = 4, column = 0, pady = 20)
        btn.grid(row = 5, column = 0, pady = 20, sticky = 'e')
        btnBack.grid(row = 5, column = 0, pady = 20, sticky = 'w')
