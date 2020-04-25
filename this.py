import os.path
from cryptography.fernet import Fernet

import os



file = open('key.key', 'rb')
key = file.read()
file.close()

# print(key)

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
            print(check_username + ", you have successfully signed in.")
            inside_user(check_username)
        else:
            print("Incorrect password.")
            login()
    else:
        print("No user under this username.")
        main()

def inside_user(username):
    # read_accounts(username)
    print("************************")
    print("Commands:")
    print("+ = add new account")
    print("************************")
    action = input("What would you like to do? ")
    if action == "+":
        add_accounts(username)

def add_accounts(username):
    new_account = input("What is the account for? ")
    new_username = input("What is the username for this account? ")
    new_password = input("What is the password for this account? ")
    password = new_password.encode()
    read_password = f.encrypt(password)
    file = open('{}.txt'.format(username), 'a')
    file.write("\n" + new_account + "\n")
    file.write(new_username + "\n")
    file.close()
    file_password = open('{}.txt'.format(username), 'ab')
    file_password.write(read_password)
    file_password.close()
    inside_user(username)

def read_accounts(username):
    file = open('{}.txt'.format(username), "r")
    for i in range(10, 0, -1):
        j = i - 1
        if j != 0 and j%3 == 0:
            answer = j
            accounts = file.readline(answer)
            print(accounts)



main()