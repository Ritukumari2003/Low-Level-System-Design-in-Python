from notification_channel import NotificationChannel

class EmailService(NotificationChannel):
    def send(self, mssg):
        print(f"Sending Email: {mssg}")