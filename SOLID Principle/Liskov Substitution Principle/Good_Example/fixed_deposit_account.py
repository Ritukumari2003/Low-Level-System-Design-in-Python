from bank_account import BankAccount

class FixedDepositAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited amount Rs. {amount}. Total balance: Rs. {self.balance}")
