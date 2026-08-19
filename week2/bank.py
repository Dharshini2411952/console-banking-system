from account import Account, Transaction
from storage import accounts, transactions, customer_index


# CREATE ACCOUNT
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

    account = Account(acc_id, name, balance)

    accounts[acc_id] = account

    # Add account ID to customer index
    customer_index[name].append(acc_id)

    print("Account Created Successfully")


# DEPOSIT
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
    print("New Balance:", accounts[acc_id].balance)


# WITHDRAW
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
    print("New Balance:", accounts[acc_id].balance)


# BALANCE CHECK
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


# CLOSE ACCOUNT
def close_account():
    acc_id = int(input("Enter Account ID: "))

    if acc_id not in accounts:
        print("Account Not Found")
        return

    account = accounts[acc_id]

    # Remove from customer index
    customer_index[account.name].remove(acc_id)

    # Remove empty customer entry
    if len(customer_index[account.name]) == 0:
        del customer_index[account.name]

    # Remove account
    del accounts[acc_id]

    # Remove transaction history
    if acc_id in transactions:
        del transactions[acc_id]

    print("Account Closed Successfully")


# VIEW ALL ACCOUNTS
def view_all_accounts():
    if not accounts:
        print("No Accounts Available")
        return

    print("\n----- ALL ACCOUNTS -----")

    for account in accounts.values():
        print("------------------------")
        print("Account ID :", account.acc_id)
        print("Name       :", account.name)
        print("Balance    :", account.balance)


# TRANSFER MONEY
def transfer():
    from_id = int(input("Enter Sender Account ID: "))
    to_id = int(input("Enter Receiver Account ID: "))

    # Check both accounts before changing balance
    if from_id not in accounts:
        print("Sender Account Not Found")
        return

    if to_id not in accounts:
        print("Receiver Account Not Found")
        return

    if from_id == to_id:
        print("Cannot transfer to the same account")
        return

    amount = float(input("Enter Transfer Amount: "))

    if amount <= 0:
        print("Invalid Amount")
        return

    if amount > accounts[from_id].balance:
        print("Insufficient Balance")
        return

    try:
        # Withdraw from sender
        accounts[from_id].balance -= amount

        # Deposit to receiver
        accounts[to_id].balance += amount

        # Create transaction
        transaction = Transaction(from_id, to_id, amount)

        # Store transaction for both accounts
        transactions[from_id].append(transaction)
        transactions[to_id].append(transaction)

        print("Transfer Successful")
        print("Sender Balance:", accounts[from_id].balance)

    except:
        # Rollback if something goes wrong
        accounts[from_id].balance += amount
        accounts[to_id].balance -= amount

        print("Transfer Failed")


# REVERSE LAST TRANSACTION
def reverse_last_transaction():
    acc_id = int(input("Enter Account ID: "))

    if acc_id not in accounts:
        print("Account Not Found")
        return

    if not transactions[acc_id]:
        print("No Transaction Available to Reverse")
        return

    # Get last transaction
    transaction = transactions[acc_id].pop()

    from_id = transaction.from_id
    to_id = transaction.to_id
    amount = transaction.amount

    # Check both accounts
    if from_id not in accounts or to_id not in accounts:
        print("Cannot Reverse Transaction")
        return

    # Reverse the transfer
    accounts[from_id].balance += amount
    accounts[to_id].balance -= amount

    # Remove same transaction from the other account's history
    if transactions[to_id]:
        transactions[to_id].pop()

    print("Last Transaction Reversed Successfully")
    print("Reversed Amount:", amount)


# FIND CUSTOMER ACCOUNTS
def find_customer_accounts():
    name = input("Enter Customer Name: ")

    if name not in customer_index:
        print("Customer Not Found")
        return

    print("\nAccounts belonging to", name)

    for acc_id in customer_index[name]:
        account = accounts[acc_id]

        print("------------------------")
        print("Account ID :", account.acc_id)
        print("Balance    :", account.balance)