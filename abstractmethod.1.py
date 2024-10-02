from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number 
        self.balance = balance 
    
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class savingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.05):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
class checkingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
        else:
            print("Transaction declined : Insufficient funds")

savings = savingsAccount('SA123', 1000)
checking = checkingAccount('CA123', 500)


savings.deposit(200)
savings.withdraw(500)
savings.withdraw(800)  # This will print "Insufficient funds"

checking.deposit(100)
checking.withdraw(550)
checking.withdraw(100)  # This will print "Transaction declined : Insufficient funds"

# Print balances
print(f"Savings Balance: {savings.balance}")
print(f"Checking Balance: {checking.balance}")
