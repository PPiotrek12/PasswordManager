from tkinter import *
from AddAccount import AddAccount
from SeeAccount import SeeAccount
import values

class Menu:
    def seeButtonClicked(self):
        self.menu_frame.pack_forget()
        see = SeeAccount(self.root, self.menu_frame)
    def addButtonClicked(self):
        self.menu_frame.pack_forget()
        add = AddAccount(self.root, self.menu_frame)
    def changeButtonClicked(self):
        pass

    def deleteButtonClicked(self):
        pass

    def __init__(self, root):
        self.root = root
        self.menu_frame = Frame(self.root)
        self.menu_frame.pack()

        seeButton = Button(
            self.menu_frame, command = self.seeButtonClicked,
            text = "See account's data",
            height = 8, width = 25
            )
        addButton = Button(
            self.menu_frame, command = self.addButtonClicked,
            text = "Add new account",
            height = 8, width = 25
            )

        changeButton = Button(
            self.menu_frame, command = self.changeButtonClicked,
            text = "Change an existing account",
            height = 8, width = 25
            )
        deleteButton = Button(
            self.menu_frame, command = self.deleteButtonClicked,
            text = "Delete an existing account",
            height = 8, width = 25
            )
        exitButton = Button(
            self.menu_frame, command = lambda: self.root.quit(),
            text = "Exit",
            height = 2, width = 20
        )
        Label(self.menu_frame, text = "Welcome to PasswordManager!", font = "Helvetica 25 bold").grid(row = 0, column = 0, columnspan = 2, pady = 20)
        seeButton.grid(row = 1, column = 0, padx = 20, pady = 20)
        addButton.grid(row = 1, column = 1)
        changeButton.grid(row = 2, column = 0)
        deleteButton.grid(row = 2, column = 1)
        exitButton.grid(row = 3, column = 0, columnspan = 2, pady = 50)
