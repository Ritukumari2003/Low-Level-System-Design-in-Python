from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance: int):
        self.balance = balance

    @abstractmethod
    def deposit(self):
        pass
