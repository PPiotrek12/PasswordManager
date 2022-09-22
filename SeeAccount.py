from Accounts import Accounts
from Encryption import Encryption

class SeeAccount(Accounts):
    def __init__(self, key1):
        super().__init__(key1)
    def seeAccount(self):
        print("Insert the number of service of which you would like to see login and password.")
        for i, act in enumerate(self.servicesList):
            print(f"[{i+1}] {act}")
        number = int(input(">>> "))
        print("")
        while number <= 0 or number >= len(self.servicesList):
            number = int(input(f"Try again. Please insert number from range [1, {len(self.servicesList)}].\n>>> "))
            print("")

        file = open(self.path + self.servicesList[number - 1] + ".txt", 'r')
        encLogin = file.readline()
        encPassword = file.readline()
        file.close()
        encLogin = encLogin[:len(encLogin)-1]
        encPassword = encPassword[:len(encPassword)-1]

        enc = Encryption(self.key1)
        login = enc.decrypt(encLogin)
        password = enc.decrypt(encPassword)

        print(f"{self.servicesList[number - 1]}:\nLogin: {login}\nPassword: {password}\n")
