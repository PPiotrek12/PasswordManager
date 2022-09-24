from Accounts import Accounts
from Encryption import Encryption
import getpass

class ChangeAccount(Accounts):
    def __init__(self, key1, key2):
        super().__init__()
        self.key2 = key2
        self.key1 = key1

    def changeAccount(self):
        number = super().printChoiceList("Insert the number of account which you would like to change.")
        if number == -1:
            return

        serviceName = self.servicesList[number - 1]
        accLogin = input("Insert new login to your account.\n>>> ")
        accPassword = getpass.getpass(prompt = "Insert new password to your account (text is hidden).\n>>> ")

        enc = Encryption(self.key1, self.key2)
        encAccLogin = enc.encrypt(accLogin)
        encAccPassword = enc.encrypt(accPassword)

        newFile = open(self.path + serviceName + ".txt", 'w')
        print(encAccLogin, file = newFile)
        print(encAccPassword, file = newFile)
        newFile.close()

        print("You have successfully changed account's data.\n\n")
