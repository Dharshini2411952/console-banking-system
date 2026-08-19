from account import Account
from storage import accounts

def create_account():
    acc_id = int(input("Enter Account ID: "))

    if acc_id in accounts:
        print("Account ID already exists!")
        return

    name = input("Enter Customer Name: ")
    balance = float(input("Enter Initial Balance: "))

    if balance < 0:
        print("Invalid Balance!")
        return

    accounts[acc_id] = Account(acc_id, name, balance)

    print("Account Created Successfully")


def deposit():
    acc_id = int(input("Enter Account ID: "))

    if acc_id not in accounts:
        print("Account Not Found")
        return

    amount = float(input("Enter Deposit Amount: "))

    if amount <= 0:
        print("Invalid Amount")
        return

    accounts[acc_id].balance += amount

    print("Deposit Successful")


def withdraw():
    acc_id = int(input("Enter Account ID: "))

    if acc_id not in accounts:
        print("Account Not Found")
        return

    amount = float(input("Enter Withdraw Amount: "))

    if amount <= 0:
        print("Invalid Amount")
        return

    if amount > accounts[acc_id].balance:
        print("Insufficient Balance")
        return

    accounts[acc_id].balance -= amount

    print("Withdrawal Successful")


def balance_check():
    acc_id = int(input("Enter Account ID: "))

    if acc_id not in accounts:
        print("Account Not Found")
        return

    account = accounts[acc_id]

    print("\n----- Account Details -----")
    print("Account ID :", account.acc_id)
    print("Name       :", account.name)
    print("Balance    :", account.balance)


def close_account():
    acc_id = int(input("Enter Account ID: "))

    if acc_id not in accounts:
        print("Account Not Found")
        return

    del accounts[acc_id]

    print("Account Closed Successfully")


def view_all_accounts():
    if not accounts:
        print("No Accounts Available")
        return

    print("\n----- All Accounts -----")

    for account in accounts.values():
        print("------------------------")
        print("Account ID :", account.acc_id)
        print("Name       :", account.name)
        print("Balance    :", account.balance)