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

    Label(keys_frame, text = "Insert first encryption key.").grid(row = 0, column = 0)
    entry1 = Entry(keys_frame)
    entry1.grid(row = 1, column = 0)
    Label(keys_frame, text = "Insert second encryption key.").grid(row = 2, column = 0)
    entry2 = Entry(keys_frame)
    entry2.grid(row = 3, column = 0)

    btn = Button(keys_frame, text = "Confirm", command = lambda: inserted(root, keys_frame, entry1, entry2))
    btn.grid(row = 4, column = 0)
