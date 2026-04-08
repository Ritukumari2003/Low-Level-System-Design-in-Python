from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def work(self):
        pass

class Worker(Employee):
    def eat(self):
        print("Worker is eating")

    def work(self):
        print("Worker is working")
        
class Robot(Employee):
    def eat(self):
        raise Exception("Robbot Cannot Eat")

    def work(self):
        print("Robot is working")

w = Worker()
w.eat()
w.work()

r = Robot()
r.work()
r.eat()
