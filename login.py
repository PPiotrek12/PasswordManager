import hashlib
import values
import getpass

def check(fileHash):
    #password = input("Insert your password.\n>>> ")
    password = getpass.getpass(prompt = "Insert your password (text is hidden).\n>>> ")
    hash = hashlib.new('sha256')
    hash.update(password.encode())
    return fileHash == hash.hexdigest()

def register():
    getpass.getpass(prompt = "Hi! I see you're new here. Please insert new password to the app which will secure your data (text is hidden).\n>>> ")
    getpass.getpass(prompt = "Now confirm password\n>>> ")
    print("")
    while password1 != password2:
        getpass.getpass(prompt = "Passwords doesn't match, try again.\n>>> ")
        getpass.getpass(prompt = "Confirm password\n>>> ")
        print("")
    hash = hashlib.new('sha256')
    hash.update(password1.encode())

    file = open(values.data_path + "login.txt", 'w')
    print(hash.hexdigest(), file=file)
    file.close()

    print("You are registered, can log in now.\n")

def login():
    try:
         file = open(values.data_path + "login.txt", 'r')
    except:
        register()

    file = open(values.data_path + "login.txt", 'r')
    fileHash = file.readline()
    file.close()
    fileHash = fileHash[:len(fileHash)-1]

    passed = False
    for i in range(3):
        correct = check(fileHash)
        if correct:
            passed = True
            break
        else:
            print("Invalid password, try again.\n")
    if not passed:
        print("You inserted invalid password three times.\n")
        return False
    print("")
    print("You are logged in!\n")
    return True
