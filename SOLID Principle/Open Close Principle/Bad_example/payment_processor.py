
class PaymentProcessor:
    def pay(self, payment_method:str, amount:int):
        if payment_method == "UPI":
            print(f"Starting UPI transaction of Rs. {amount}")
            print("UPI transaction finished")
        elif payment_method == "credit_card":
            print(f"Starting credit card transaction of Rs. {amount}")
            print("Credit Card transaction finished")
        elif payment_method == "net_banking":
            print(f"Starting net banking transaction of Rs. {amount}")
            print("New banking transaction finished")

        # We will need to make changes in the existing code if we need to add any new method of payment : It will violate the OCP principle which says the code should be open for extension but closed for modification

pay_p = PaymentProcessor()
pay_p.pay("credit_card", 2000)


