class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def show_balance(self):
        print(f"Current balance: {self.balance}")

  # Create an account with initial balance of 100
account = BankAccount("Amadou", 100)

account.deposit(50)     # balance becomes 150
account.withdraw(30)    # balance becomes 120
account.show_balance()  # prints: Current balance: 120       