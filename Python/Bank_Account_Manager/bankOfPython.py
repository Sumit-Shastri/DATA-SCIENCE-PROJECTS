import json
import os


class manager:
    def createAccount(self):
        print("Creating account")
        userName = input("Enter your name : ")

        filename = f"{userName}.json"
        if os.path.exists(filename):
            print("Username exists , please try another")
            manager.createAccount()
        userNumber = input("Enter your number : ")
        userGmail = input("Enter your gmail : ")
        while True:
            createUserPassword = input("Create Password : ")
            userPassword = input("Re-Enter Password : ")
            if userPassword != createUserPassword:
                print("Invalid password , retry")
            else:
                python_data = {
                    "userName": userName,
                    "userNumber": userNumber,
                    "userGmail": userGmail,
                    "userPassword": userPassword,
                    "Balance" : 0,
                    "Transaction History" : []
                }

                try:
                    with open(f'{userName}.json', 'w') as file:
                        json.dump(python_data, file, indent=4)
                    print("Data successfully written to 'output.json'.")
                except IOError:
                    print("Error: Could not write to 'output.json'.")
                print("*** Account Created Successfully ***")
                main()
                break
    def login(self):
        print("***   Login   ***")
        userName = input("Enter userName : ")
        filename = f"{userName}.json"
        if os.path.exists(filename):
            with open(f"{filename}", "r") as f:
                data = json.load(f)
            stored_password = data["userPassword"]
            userPassword = input("Enter Password : ")
            if userPassword == stored_password:
                print("Login Succesfull")

            else:
                print("fuck off")
        else:
            print("fuck Off")

    def afterLogin(self):
        print(m.menu)
        choice = int(input("Enter your Choice : "))
        if choice == 1:
            manager.deposit()
        elif choice == 2:
            manager.withdraw()
        elif choice == 3:
            manager.send()
        elif choice == 4:
            manager.checkBalance()
        elif choice == 5:
            manager.settings()

    def deposit(self):
        print("Deposit")
        amount = int(input("Enter amount : "))

    def withdraw(self):
        print("Withdraw")
    def send(self):
        print('Send')
    def checkBalance(self):
        print("Check balance")
    def settings(self):
        print("Settings"),

manager = manager()

class messages:
    msg1 = "How do I Help You ??\n"
    menu = """
1. Deposit Money
2. Withdraw Money
3. Send Money
4. Check Balance
5. Settings\n\n"""
    menu2 = '''1. create Account
2. login'''

m = messages()

def main():
    print("***   Welcome to Bank Of Python   ***\n")
    print(m.msg1)
    print(m.menu2)
    while True:
        try:
            choice = int(input("Enter Your choice : "))
            if choice == 1:
                manager.createAccount()
            elif choice == 2:
                manager.login()
            else:
                print("Invalid Choice , Try Again")
                break
        except ValueError:
            print("Please enter a valid number (1-6).\n")

main()