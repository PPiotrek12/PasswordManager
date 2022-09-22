from Encryption import Encryption
from Login import login

def start():
	if not login():
		return

start()
