from tkinter import *
import values

def seeButtonClicked(root, frame):
    pass
def addButtonClicked(root, frame):
    pass
def changeButtonClicked(root, frame):
    pass
def deleteButtonClicked(root, frame):
    pass

def menu(root):
    menu_frame = Frame(root)
    menu_frame.pack()

    seeButton = Button(
        menu_frame,
        text = "See account's data",
        command = lambda: seeButtonClicked(root, menu_frame),
        height = 8,
        width = 25
        )
    addButton = Button(
        menu_frame,
        text = "Add new account",
        command = lambda: addButtonClicked(root, menu_frame),
        height = 8,
        width = 25
        )

    changeButton = Button(
        menu_frame,
        text = "Change an existing account",
        command = lambda: changeButtonClicked(root, menu_frame),
        height = 8,
        width = 25
        )
    deleteButton = Button(
        menu_frame,
        text = "Delete an existing account",
        command = lambda: deleteButtonClicked(root, menu_frame),
        height = 8,
        width = 25
        )
    exitButton = Button(
        menu_frame,
        text = "Exit",
        command = lambda: root.quit(),
        height = 2,
        width = 20
    )
    Label(menu_frame, text = "Welcome to PasswordManager!", font = "Helvetica 25 bold").grid(row = 0, column = 0, columnspan = 2, pady = 20)
    seeButton.grid(row = 1, column = 0, padx = 20, pady = 20)
    addButton.grid(row = 1, column = 1)
    changeButton.grid(row = 2, column = 0)
    deleteButton.grid(row = 2, column = 1)
    exitButton.grid(row = 3, column = 0, columnspan = 2, pady = 50)
