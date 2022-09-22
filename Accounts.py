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
test = Accounts()
