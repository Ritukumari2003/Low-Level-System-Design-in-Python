# Invoker : Waiter
# Invoker doesn't need to know what order has been place

from command_interface import Order

class Waiter:
    def take_order(self, order: Order):
        order.execute_order()