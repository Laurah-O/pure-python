# Base class
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Invalid withdrawal amount or insufficient funds"

    def get_balance(self):
        return f"Account balance: {self.balance}"

# Derived class for Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest added: {interest}. New balance: {self.balance}"

# Derived class for Checking Account
class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=500.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Invalid withdrawal amount or exceeds overdraft limit"

# Usage example
savings = SavingsAccount("123456", "Laura", 1000.0)
print(savings.deposit(500))
print(savings.add_interest())
print(savings.get_balance())

checking = CheckingAccount("654321", "Adrian", 500.0)
print(checking.withdraw(100))
print(checking.withdraw(1000))
print(checking.get_balance())