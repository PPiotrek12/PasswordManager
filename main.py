from Encryption import Encryption
from Login import login

def start():
	if not login():
		return

	key1 = input("Insert first encription key.\n>>> ")
	print("\n")

	choice = input("""What do you want to do?
[1] Add new account.
[2] See login and password to the existing account.
[3] Change an existing account
[4] Remove an existing account.
>>> """)

	
start()
