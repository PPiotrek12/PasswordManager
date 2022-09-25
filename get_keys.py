from tkinter import *
import values
from menu import menu

def inserted(root, frame, entry1, entry2):
    values.key1 = entry1.get()
    values.key2 = entry2.get()

    frame.pack_forget()
    menu(root)

def get_keys(root):
    keys_frame = Frame(root)
    keys_frame.pack()

    entry1 = Entry(keys_frame, width = 53)
    entry2 = Entry(keys_frame, width = 53)
    Label(keys_frame, text = "Insert first encryption key.", font = "Helvetica 20 bold").grid(row = 0, column = 0, pady = 20)
    entry1.grid(row = 1, column = 0)
    Label(keys_frame, text = "Insert second encryption key.", font = "Helvetica 18 bold").grid(row = 2, column = 0, pady = 20)
    entry2.grid(row = 3, column = 0)

    btn = Button(keys_frame, text = "Confirm", command = lambda: inserted(root, keys_frame, entry1, entry2))
    btn.grid(row = 4, column = 0, pady = 30)
