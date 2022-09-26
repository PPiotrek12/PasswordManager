from tkinter import *
from tkinter import messagebox
import values

class Accounts:
    def __init__(self):
        self.servicesList = []
        try:
            servDataFile = open(values.data_path + "services.txt", 'r')
        except:
            servDataFile = open(values.data_path + "services.txt", 'w')
            servDataFile = open(values.data_path + "services.txt", 'r')
        self.servicesList = servDataFile.readlines()
        servDataFile.close()
        for i in range(len(self.servicesList)):
            self.servicesList[i] = self.servicesList[i][:len(self.servicesList[i])-1]
        self.servicesList.sort()

    def getChoiceNumber(self):
        return self.act
    def printChoiceList(self, frame):
        self.frame = frame
        if len(self.servicesList) == 0:
            messagebox.showinfo(self.frame, message = "No accounts added yet, firstly add one.")
            return -1

        self.last = -1
        self.act = -1
        btn = []
        for i, e in enumerate(self.servicesList):
            def clicked(number = i):
                if self.act == -1:
                    btn[number]['state'] = DISABLED
                else:
                    btn[self.act]['state'] = NORMAL
                    btn[number]['state'] = DISABLED
                self.last = self.act
                self.act = number

            btn.append(Button(self.frame, text = e, command = clicked, width = 20, height = 2))
            btn[i].grid(row = int(i/3) + 1, column = i % 3, pady = 5, padx = 3)
