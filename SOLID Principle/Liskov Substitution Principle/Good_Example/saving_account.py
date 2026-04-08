from withdrawable_account import WithdrawbleAccount

class SavingsAccount(WithdrawbleAccount):
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
