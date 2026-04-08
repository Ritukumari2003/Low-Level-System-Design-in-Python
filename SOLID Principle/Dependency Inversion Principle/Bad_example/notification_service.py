from email_service import EmailService
from sms_Service import SmsService

class NotificationService:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SmsService()
    
    def notify_by_email(self, mssg):
        self.email_service.sendEmail(mssg)

    def notify_by_sms(self, mssg):
        self.sms_service.sendSMS(mssg)

ns = NotificationService()
ns.notify_by_email("Good Morning")
ns.notify_by_sms("Hello")
    