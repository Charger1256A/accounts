import os.path
from cryptography.fernet import Fernet
import linecache
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
    read_accounts(username)
    print("Newly created accounts won't display until you restart the program")
    print("***********************************************************")
    print("Commands:")
    print("+ = add new account")
    print("Enter number corresponding with account to view details.")
    print("***********************************************************")
    action = input("What would you like to do? ")
    if action == "+":
        add_accounts(username)
    elif type(int(action)) == int:
        specific_accounts(username, action)

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
    arr = []
    file = open('{}.txt'.format(username), "r")
    num = 0
    for i in range(10000, 0, -1):
        j = i - 1
        if j != 0 and j % 3 == 0 and linecache.getline('{}.txt'.format(username), j) != "":
            num += 1
            accounts = j - 1
            # arr.append(accounts)
            read_accounts = linecache.getline('{}.txt'.format(username), accounts)
            print(str(num) + ") " + read_accounts)
    #
    # sa = arr[int(account) - 1]
    # su = sa + 1
    # print()


def specific_accounts(username, account):
    arr = []
    file = open('{}.txt'.format(username), "r")
    for i in range(10000, 0, -1):
        j = i - 1
        if j != 0 and j % 3 == 0 and linecache.getline('{}.txt'.format(username), j) != "":
            accounts = j - 1
            arr.append(accounts)
    sa = arr[int(account) - 1]
    su = sa + 1
    sp = sa + 2
    spec_account = linecache.getline('{}.txt'.format(username), sa)
    spec_username = linecache.getline('{}.txt'.format(username), su)


    print("Account: " + spec_account)
    print("    Username: " + spec_username)

    file.close()
    file_1 = open('{}.txt'.format(username), "rb")

    spec_password = linecache.getline('{}.txt'.format(username), sp).encode()
    # print(spec_password)
    read_password = (f.decrypt(spec_password)).decode()
    print("    Password: " + read_password)
    file_1.close()
    inside_user(username)

main()