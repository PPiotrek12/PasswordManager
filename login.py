import hashlib
import values

def check():
    password = input("Insert your password.\n>>> ")
    hash = hashlib.new('sha256')
    hash.update(password.encode())
    return values.login_password_hash == hash.digest()
def login():
    passed = False
    for i in range(3):
        correct = check()
        if correct:
            passed = True
            break
        else:
            print("Invalid password, try again.\n")
    if not passed:
        print("You inserted invalid password three times.\n")
        return False
    print("You are logged in successfully.\n")
    return True
