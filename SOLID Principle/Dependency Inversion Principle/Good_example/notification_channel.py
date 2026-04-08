from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    @abstractmethod
    def send(mssg):
        pass