
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: int):
        pass

class UPIPayment(PaymentMethod):
    def pay(self, amount:int):
        print(f"Paying Rs. {amount} through UPI")

class CreditCardPayment(PaymentMethod):
    def pay(self, amount:int):
        print(f"Paying Rs. {amount} through Credit Card")

class DebitCardPayment(PaymentMethod):
    def pay(self, amount:int):
        print(f"Paying Rs. {amount} through Debit Card")

# Adding new payment method of paypal without making changes in actual code
class Paypal(PaymentMethod):
    def pay(self, amount:int):
        print(f"Paying Rs. {amount} through Paypal")

class PaymentProcessor:
    def process_payment(self, payment_method: PaymentMethod, amount: int):
        payment_method.pay(amount)

debit = DebitCardPayment()
credit = CreditCardPayment()

pay_processor = PaymentProcessor()
pay_processor.process_payment(credit, 100000)


