
class DiscountService:
    def calculate_discount(self, discount_type: str):
        if discount_type == "diwali":
            print("Applying diwali discount of 20%")
        elif discount_type == "first_order":
            print("Applying first order discount of 15%")
        else:
            print("No discount allowed")

discount_service = DiscountService()
discount_service.calculate_discount("diwali")
discount_service.calculate_discount("holi")