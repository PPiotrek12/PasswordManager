from AddAccount import AddAccount
from DeleteAccount import DeleteAccount
from SeeAccount import SeeAccount
from ChangeAccount import ChangeAccount
from login import login
import getpass

def start():
	if not login():
		return

	key1 = getpass.getpass(prompt = "Insert first encryption key (text is hidden).\n>>> ")
	print("")

	key2 = getpass.getpass(prompt = "Insert second encryption key (text is hidden).\n>>> ")
	print("")

	while True:
		choice = int(input("""What do you want to do?
[1] See login and password to the existing account.
[2] Add new account.
[3] Change an existing account
[4] Delete an existing account.
[5] Exit.
>>> """))
		print("")
		while choice <= 0 or choice >= 6:
			choice = int(input(f"Try again. Please insert number from range [1, 5].\n>>> "))
			print("")

		if choice == 1:
			see = SeeAccount(key1, key2)
			see.seeAccount()
		elif choice == 2:
			add = AddAccount(key1, key2)
			add.addAccount()
		elif choice == 3:
			cha = ChangeAccount(key1, key2)
			cha.changeAccount()
		elif choice == 4:
			dele = DeleteAccount()
			dele.deleteAccount()
		else:
			return
		choice2 = int(input("Do you want to continue[1] or exit[2]?\n>>> "))
		if choice2 == 2:
			return
		print("")
start()
