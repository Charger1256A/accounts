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
        file.write(password)
        file.close()


        print("You have succesfully logged in!")
        login()


def login():
    pass

main()