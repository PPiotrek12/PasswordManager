from tkinter import *
import hashlib
import values
from get_keys import get_keys

def check(root, frame, entry, fileHash):
    password = entry.get()
    hash = hashlib.new('sha256')
    hash.update(password.encode())
    if fileHash != hash.hexdigest():
        Label(frame, text = "Wrong password, try again.").grid(row = 3, column = 0)
    else:
        frame.pack_forget()
        get_keys(root)

def login(root):
    file = open(values.data_path + "login.txt", 'r')
    fileHash = file.readline()
    file.close()
    fileHash = fileHash[:len(fileHash)-1]

    login_frame = Frame(root)
    login_frame.pack()
    Label(login_frame, text = "Insert your password.").grid(row = 0, column = 0)
    entry = Entry(login_frame)
    entry.grid(row = 1, column = 0)
    btn = Button(login_frame, text = "Login", command = lambda: check(root, login_frame, entry, fileHash))
    btn.grid(row = 2, column = 0)
