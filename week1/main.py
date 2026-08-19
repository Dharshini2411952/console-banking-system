from week1.bank import *

while True:

    print("\n========== BANK MENU ==========")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Balance Check")
    print("5. Close Account")
    print("6. View All Accounts")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        balance_check()

    elif choice == "5":
        close_account()

    elif choice == "6":
        view_all_accounts()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")