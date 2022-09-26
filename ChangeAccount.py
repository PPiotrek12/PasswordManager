from Accounts import Accounts
from tkinter import *
from Encryption import Encryption
from ChangeAccount2 import ChangeAccount2

class ChangeAccount(Accounts):
    def back_to_menu(self):
        self.change_account_frame.pack_forget()
        self.menu_frame.pack()

    def changeAccount(self):
        number = super().getChoiceNumber()
        if number == -1:
            return
        self.change_account_frame.pack_forget()
        change2 = ChangeAccount2(self.root, self.change_account_frame, number)

    def __init__(self, root, menu_frame):
        super().__init__()
        self.root = root
        self.menu_frame = menu_frame
        self.change_account_frame = Frame(self.root)
        self.change_account_frame.pack()

        Label(self.change_account_frame,
        text = "Select which service's \ndata you would like to change", font = "Helvetica 20 bold").grid(row = 0, column = 0, pady = 20)

        number = super().printChoiceList(self.change_account_frame)
        if number == -1:
            self.back_to_menu()
            return

        btnChange = Button(self.change_account_frame, text = "Change", command = self.changeAccount, width = 14)
        btnBack = Button(self.change_account_frame, text = "Back to menu", command = self.back_to_menu, width = 14)
        btnChange.grid(row = len(self.servicesList) + 2, column = 0, pady = 20, sticky = 'e')
        btnBack.grid(row = len(self.servicesList) + 2, column = 0, pady = 20, sticky = 'w')