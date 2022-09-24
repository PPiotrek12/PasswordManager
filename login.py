import hashlib
import values

def check(fileHash):
    password = input("Insert your password.\n>>> ")
    hash = hashlib.new('sha256')
    hash.update(password.encode())
    return fileHash == hash.hexdigest()

def register():
    password1 = input("Hi! I see you're new here. Please insert new password to the app which will secure your data.\n>>> ")
    password2 = input("Now confirm password\n>>> ")
    print("")
    while password1 != password2:
        password1 = input("Passwords doesn't match, try again.\n>>> ")
        password2 = input("Confirm password\n>>> ")
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
    print("You are logged in!\n")
    return True
