from saving_account import SavingsAccount
from fixed_deposit_account import FixedDepositAccount

print("Saving Account: ")
saving_acc = SavingsAccount(1000)
saving_acc.deposit(500)
saving_acc.withdraw(500)

print("Fixed Deposit Account: ")
fd_acc = FixedDepositAccount(10000)
fd_acc.deposit(200)
