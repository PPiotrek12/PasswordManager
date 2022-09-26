from tkinter import *
from Accounts import Accounts
from Encryption import Encryption

class SeeAccount(Accounts):
    def __init__(self, root, menu_frame):
        super().__init__()
        self.root = root
        self.menu_frame = menu_frame
        self.see_account_frame = Frame(root)
        self.see_account_frame.pack()

        Label(self.see_account_frame, text = "Select which service's \ndata you would like to see", font = "Helvetica 20 bold").grid(row = 0, column = 0, pady = 20)

        number = super().printChoiceList(self.see_account_frame, "Insert the number of account of which you would like to see login and password.")
        if number == -1:
            self.see_account_frame.pack_forget()
            self.menu_frame.pack()
            return

    def seeAccount(self):

        file = open(self.path + self.servicesList[number - 1] + ".txt", 'r')
        encLogin = file.readline()
        encPassword = file.readline()
        file.close()
        encLogin = encLogin[:len(encLogin)-1]
        encPassword = encPassword[:len(encPassword)-1]

        enc = Encryption(self.key1, self.key2)
        login = enc.decrypt(encLogin)
        password = enc.decrypt(encPassword)

        print(f"{self.servicesList[number - 1]} account's data:\nLogin: {login}\nPassword: {password}\n\n")
