from tkinter import *
from tkinter import messagebox
from Accounts import Accounts
import os
import values

class DeleteAccount(Accounts):
    def back_to_menu(self):
        self.delete_account_frame.pack_forget()
        self.menu_frame.pack()

    def deleteAccount(self):
        number = super().getChoiceNumber()
        if number == -1:
            return

        decision = messagebox.askyesno(message = f"Are you completely sure you want delete {self.servicesList[number - 1]} account's data?")
        if not decision:
            error = Label(self.delete_account_frame, text = "Accunt hasn't been deleted.", fg = "red")
            error.grid(row = len(self.servicesList) + 3, column = 0, columnspan = 3)
            return

        os.remove(values.data_path + self.servicesList[number] + ".txt")
        self.servicesList.pop(number)
        file = open(values.data_path + "services.txt", 'w')
        for i in self.servicesList:
            print(i, file = file)
        file.close()

        messagebox.showinfo(message = "Your account has been deleted successfully.")
        self.back_to_menu()

    def __init__(self, root, menu_frame):
        super().__init__()
        self.root = root
        self.menu_frame = menu_frame
        self.delete_account_frame = Frame(root)
        self.delete_account_frame.pack()

        Label(self.delete_account_frame,
        text = "Select which service\n you would like to delete", font = "Helvetica 20 bold").grid(row = 0, column = 0, columnspan = 3, pady = 20)

        number = super().printChoiceList(self.delete_account_frame)
        if number == -1:
            self.back_to_menu()
            return

        btnDelete = Button(self.delete_account_frame, text = "Delete", command = self.deleteAccount, width = 14)
        btnBack = Button(self.delete_account_frame, text = "Back to menu", command = self.back_to_menu, width = 14)
        btnBack.grid(row = len(self.servicesList) + 2, column = 0, pady = 20, sticky = 'w')
        btnDelete.grid(row = len(self.servicesList) + 2, column = 2, pady = 20, sticky = 'e')
