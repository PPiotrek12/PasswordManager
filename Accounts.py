import values
class Accounts:
    path = values.data_path
    def __init__(self):
        self.servicesList = []
        servDataFile = open(self.path + "services.txt", 'r')
        self.servicesList = servDataFile.readlines()
        servDataFile.close()
        for i in range(len(self.servicesList)):
            self.servicesList[i] = self.servicesList[i][:len(self.servicesList[i])-1]

    def printChoiceList(self, text):
        if len(self.servicesList) == 0:
            print("No accounts added yet, firstly add one.\n\n")
            return -1
        print(text)
        for i, act in enumerate(self.servicesList):
            print(f"[{i+1}] {act}")
        number = int(input(">>> "))
        print("")
        while number <= 0 or number > len(self.servicesList):
            number = int(input(f"Try again. Please insert number from range [1, {len(self.servicesList)}].\n>>> "))
            print("")
        return number
