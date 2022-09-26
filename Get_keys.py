from tkinter import *
import values
from Menu import Menu

class Get_keys:
    def inserted(self):
        values.key1 = self.entry1.get()
        values.key2 = self.entry2.get()

        self.keys_frame.pack_forget()
        menu = Menu(self.root)

    def __init__(self, root):
        self.root = root
        self.keys_frame = Frame(self.root)
        self.keys_frame.pack()

        self.entry1 = Entry(self.keys_frame, width = 53, show = '*')
        self.entry2 = Entry(self.keys_frame, width = 53, show = '*')
        btn = Button(self.keys_frame, text = "Confirm", command = self.inserted)

        Label(self.keys_frame, text = "Insert first encryption key.", font = "Helvetica 20 bold").grid(row = 0, column = 0, pady = 20)
        self.entry1.grid(row = 1, column = 0)
        Label(self.keys_frame, text = "Insert second encryption key.", font = "Helvetica 18 bold").grid(row = 2, column = 0, pady = 20)
        self.entry2.grid(row = 3, column = 0)
        btn.grid(row = 4, column = 0, pady = 30)
