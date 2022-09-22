from AddAccount import AddAccount
from login import login

def start():
	if not login():
		return

	key1 = input("Insert first encription key.\n>>> ")
	print("")
	while True:
		choice = int(input("""What do you want to do?
[1] See login and password to the existing account.
[2] Add new account.
[3] Change an existing account
[4] Remove an existing account.
[5] Exit.
>>> """))
		print("")
		if choice == 1:
			pass
		elif choice == 2:
			add = AddAccount(key1)
			add.addAccount()
		elif choice == 3:
			pass
		elif choice == 4:
			pass
		else:
			return
		choice2 = int(input("Do you want to continue[1] or exit[2]?\n>>> "))
		if choice2 == 2:
			return
		print("")
start()
