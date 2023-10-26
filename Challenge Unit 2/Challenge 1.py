class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Balance: ${self.__account_balance}")


# Testing the BankAccount class
if __name__ == "__main__":
    # Create an instance of the BankAccount class
    account = BankAccount("1234567890", "John Doe", 1000.0)

    # Display account details
    account.display_balance()

    # Deposit money
    account.deposit(1000.0)

    # Withdraw money
    account.withdraw(500.0)

    # Attempt to withdraw more than the balance
    account.withdraw(2000.0)