import os.path
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os



file = open('key.key', 'rb')
key = file.read()
file.close()
# print(key)


# print(hashlib.algorithms_available)
# tr = hashlib.md5(b'Hello World')
# final = tr.hexdigest()
# print(final)

f = Fernet(key)
def main():

    choice = input("Would you like to signup or login? ")
    if choice == "signup" or choice == "Signup" or choice == "s":
        signup()
    else:
        login()
def signup():
    create_username = input("What would you like your username to be? ")
    create_password = input("What would you like your password to be? ")
    password = create_password.encode()
    read_password = f.encrypt(password)


    # print(password_secret)
    if os.path.isfile('{}.txt'.format(create_username)):
        print("There is already an account under this username.")
        login()
    else:
        file = open('{}.txt'.format(create_username), 'wb')
        file.write(read_password)
        file.close()

        print("You're account has been created")
        login()


def login():
    check_username = input("Enter Username: ")
    check_password = input("Enter Password: ")

    if os.path.isfile('{}.txt'.format(check_username)):
        file = open('{}.txt'.format(check_username), 'rb')
        compare_password = file.read()
        read_password = (f.decrypt(compare_password)).decode()
        if check_password == read_password:
            print("You have succesfully signed in.")
        else:
            print("incorrectpassword.")
            login()
    else:
        print("No user under this username.")
        main()

main()