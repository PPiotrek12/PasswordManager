from Accounts import Accounts
from Encryption import Encryption

class SeeAccount(Accounts):
    def __init__(self, key1):
        super().__init__()
        self.key1 = key1

    def seeAccount(self):
        number = super().printChoiceList("Insert the number of service of which you would like to see login and password.")
        if number == -1:
            return 

        file = open(self.path + self.servicesList[number - 1] + ".txt", 'r')
        encLogin = file.readline()
        encPassword = file.readline()
        file.close()
        encLogin = encLogin[:len(encLogin)-1]
        encPassword = encPassword[:len(encPassword)-1]

        enc = Encryption(self.key1)
        login = enc.decrypt(encLogin)
        password = enc.decrypt(encPassword)

        print(f"{self.servicesList[number - 1]} account's data:\nLogin: {login}\nPassword: {password}\n\n")
