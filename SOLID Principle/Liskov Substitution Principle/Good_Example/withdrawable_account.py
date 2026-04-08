from bank_account import BankAccount
from abc import abstractmethod

class WithdrawbleAccount(BankAccount):
    def __init__(self, balance: int):
        super().__init__(balance)

    @abstractmethod
    def withdraw(self, amount):
        pass
