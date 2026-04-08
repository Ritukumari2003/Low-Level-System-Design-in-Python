from notification_channel import NotificationChannel

class SMSService(NotificationChannel):
    def send(self, mssg):
        print(f"Sending SMS: {mssg}")