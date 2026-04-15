# Command : Order

from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def execute_order(self):
        pass