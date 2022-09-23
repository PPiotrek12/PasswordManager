from Accounts import Accounts
from Encryption import Encryption

class AddAccount(Accounts):
    def __init__(self, key1):
        super().__init__()
        self.key1 = key1

    def addAccount(self):
        while True:
            serviceName = input("Insert new service name.\n>>> ")
            if serviceName in self.servicesList:
                print("Such servis exists.\n")
            else:
                break
        accLogin = input("Insert login to your account.\n>>> ")
        accPassword = input("Insert password to your account.\n>>> ")

        enc = Encryption(self.key1)
        encAccLogin = enc.encrypt(accLogin)
        encAccPassword = enc.encrypt(accPassword)

        newFile = open(self.path + serviceName + ".txt", 'w')
        print(encAccLogin, file = newFile)
        print(encAccPassword, file = newFile)
        newFile.close()

        servDataFile = open(self.path + "services.txt", 'a')
        print(serviceName, file = servDataFile)
        servDataFile.close()

        print("\nWell done, your account has beed added!\n\n")
