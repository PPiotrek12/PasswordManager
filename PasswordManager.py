from AddAccount import AddAccount
from DeleteAccount import DeleteAccount
from SeeAccount import SeeAccount
from ChangeAccount import ChangeAccount
from register import register
from login import login
import values
import os.path

from tkinter import *

root = Tk()
root.geometry("500x600")

def start():
	homedir = os.path.expanduser("~") + "/"
	values.data_path = homedir + ".PasswordManager/"
	try:
		file = open(homedir + ".PasswordManager/login.txt", 'r')
		file.close()
		done = login(root)
	except:
		try:
			file = open(homedir + ".PasswordManager/login.txt", 'w')
			file.close()
			done = register(root)
		except: #directory /home/username/.PasswordManager doesn't exist and we have to add it first
			os.mkdir(homedir + ".PasswordManager")
			done = register(root)

	if not done:
		return

	return
start()
root.mainloop()
