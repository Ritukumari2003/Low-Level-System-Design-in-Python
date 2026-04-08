from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance: int):
        self.balance = balance

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Cannot withdraw!!, remaining balance Rs. {self.balance}.")
        else:
            self.balance -= amount
            print(f"Withdrawn amount Rs. {amount}. Remaining balance: Rs. {self.balance}")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited amount Rs. {amount}. Total balance: Rs. {self.balance}")

class FixedDepositAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        raise Exception("Cannot withdraw from fixed deposit account!!")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited amount Rs. {amount}. Total balance: Rs. {self.balance}")

s = SavingsAccount(1000)

s.deposit(1000)
s.withdraw(500)

f = FixedDepositAccount(1000)
f.withdraw(500)
