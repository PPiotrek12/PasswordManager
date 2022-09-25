import hashlib
import values
import getpass
from tkinter import *

def check(frame, entry, fileHash):
    password = entry.get()
    hash = hashlib.new('sha256')
    hash.update(password.encode())
    if fileHash != hash.hexdigest():
        wrong = Label(frame, text = "Wrong password, try again.").grid(row = 2, column = 0)
    else:
        print("zalogowano!!!")



def login(root):
    file = open(values.data_path + "login.txt", 'r')
    fileHash = file.readline()
    file.close()
    fileHash = fileHash[:len(fileHash)-1]

    login_frame = Frame(root)
    login_frame.pack()
    entry = Entry(login_frame)
    btn = Button(login_frame, text = "Login", command = lambda: check(login_frame, entry, fileHash))
    entry.grid(row = 0, column = 0)
    btn.grid(row = 1, column = 0)
