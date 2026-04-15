class Chef:
    def cook_pasta(self):
        print("Chef is cooking pasta")
    
    def cook_pizza(self):
        print("Chef is cooking pizza")

class Waiter:
    def __init__(self, chef: Chef):
        self.__chef = chef
    
    def place_order(self, item: str):  
        if item == "pasta":
            self.__chef.cook_pasta()
        elif item == "pizza":
            self.__chef.cook_pizza()
        # elif 
        # elif 
        # elif 
        else:
            print("Cannot place order!!..")
    
chef = Chef()
waiter = Waiter(chef)
waiter.place_order("pasta")   