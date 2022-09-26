from Register import Register
from Login import Login
import values
import os.path

from tkinter import *

class Main:
	def __init__(self):
		self.root = Tk()
		self.root.title("PasswordManager")
		self.root.geometry("680x740")

		homedir = os.path.expanduser("~") + "/"
		values.data_path = homedir + ".PasswordManager/"
		try:
			file = open(homedir + ".PasswordManager/login.txt", 'r')
			file.close()
			login = Login(self.root)
		except:
			try:
				file = open(homedir + ".PasswordManager/login.txt", 'w')
				file.close()
				register = Register(self.root)
			except: #directory /home/username/.PasswordManager doesn't exist and we have to add it first
				os.mkdir(homedir + ".PasswordManager")
				register = Register(self.root)



main = Main()
main.root.mainloop()
