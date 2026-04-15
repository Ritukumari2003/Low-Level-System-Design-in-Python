from chef import Chef
from burger_order import BurgerOrder
from pizza_order import PizzaOrder
from waiter import Waiter

chef = Chef()
pizza_order = PizzaOrder(chef)
waiter = Waiter()
waiter.take_order(pizza_order)

burger_order = BurgerOrder(chef)
waiter.take_order(burger_order)