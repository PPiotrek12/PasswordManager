from tkinter import *
from Accounts import Accounts
from Encryption import Encryption
import values

class SeeAccount(Accounts):
    def seeAccount(self):
        number = super().getChoiceNumber()
        if number == -1:
            self.error = Label(self.see_account_frame, text = "Select service.", fg = "red")
            self.error.grid(row = len(self.servicesList) + 3, column = 0, pady = 10)
        else:
            file = open(values.data_path + self.servicesList[number] + ".txt", 'r')
            encLogin = file.readline()
            encPassword = file.readline()
            file.close()
            encLogin = encLogin[:len(encLogin)-1]
            encPassword = encPassword[:len(encPassword)-1]

            enc = Encryption(values.key1, values.key2)
            login = enc.decrypt(encLogin)
            password = enc.decrypt(encPassword)

            if self.error != 0:
                self.error.destroy()
            if self.shown != 0:
                self.shown.destroy()

            self.shown = Label(self.see_account_frame,
            text = self.servicesList[number] + f" account's data:\n\nLogin: {login}\nPassword: {password}", font = "Helvetica 14")

            self.shown.grid(row = len(self.servicesList) + 4, column = 0, pady = 10)

    def back_to_menu(self):
        self.see_account_frame.pack_forget()
        self.menu_frame.pack()

    def __init__(self, root, menu_frame):
        super().__init__()
        self.root = root
        self.menu_frame = menu_frame
        self.see_account_frame = Frame(root)
        self.see_account_frame.pack()
        self.error = 0
        self.shown = 0

        Label(self.see_account_frame,
        text = "Select which service's \ndata you would like to see", font = "Helvetica 20 bold").grid(row = 0, column = 0, pady = 20)

        number = super().printChoiceList(self.see_account_frame, "Insert the number of account of which you would like to see login and password.")
        if number == -1:
            self.see_account_frame.pack_forget()
            self.menu_frame.pack()
            return

        btnSee = Button(self.see_account_frame, text = "See", command = self.seeAccount, width = 14)
        btnBack = Button(self.see_account_frame, text = "Back to menu", command = self.back_to_menu, width = 14)
        btnSee.grid(row = len(self.servicesList) + 2, column = 0, pady = 20, sticky = 'e')
        btnBack.grid(row = len(self.servicesList) + 2, column = 0, pady = 20, sticky = 'w')
