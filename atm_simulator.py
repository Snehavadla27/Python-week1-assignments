# ATM Mini Project using Functions

def check_balance(balance):
    print("Your balance is:", balance)
    return balance


def deposit(balance):
    amount = int(input("Enter amount to deposit: "))

    if amount > 0:
        balance = balance + amount
        print("Amount deposited successfully.")
        print("Updated balance:", balance)
    else:
        print("Please enter a valid amount.")

    return balance


def withdraw(balance):
    amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Please enter a valid amount.")

    elif amount <= balance:
        balance = balance - amount
        print("Please collect your cash.")
        print("Updated balance:", balance)

    else:
        print("Insufficient balance.")

    return balance


def atm():
    balance = 1000
    pin = 1234

    print("===== Welcome to ATM =====")

    entered_pin = int(input("Enter your PIN: "))

    if entered_pin != pin:
        print("Incorrect PIN.")
        print("Transaction cancelled.")
        return

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            balance = check_balance(balance)

        elif choice == 2:
            balance = deposit(balance)

        elif choice == 3:
            balance = withdraw(balance)

        elif choice == 4:
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start ATM
atm()
