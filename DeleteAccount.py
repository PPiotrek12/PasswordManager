from Accounts import Accounts
import os

class DeleteAccount(Accounts):
    def __init__(self):
        super().__init__()

    def deleteAccount(self):
        number = super().printChoiceList("Insert the number of account which you would like to delete.")
        if number == -1:
            return

        decision = input(f"Are you completely sure you want delete {self.servicesList[number - 1]} account's data? [yes\\no]\n>>> ")
        print("")
        while decision != 'yes' and decision != 'no':
            decision = input(f"Are you completely sure you want delete {self.servicesList[number - 1]} account's data? [yes\\no]\n>>> ")
            print("")

        if decision == 'no':
            print("Accunt hasn't been deleted.")
            return

        os.remove(self.path + self.servicesList[number - 1] + ".txt")

        self.servicesList.pop(number - 1)

        file = open(self.path + "services.txt", 'w')
        for i in self.servicesList:
            print(i, file = file)
        file.close()

        print("Account has been successfully deleted.\n\n")
