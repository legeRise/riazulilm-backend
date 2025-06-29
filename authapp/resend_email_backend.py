# resend_email_backend.py (RESEND email service 3000/mails per month free)
import requests
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail import EmailMessage
from django.conf import settings

class ResendEmailBackend(BaseEmailBackend):
    """
    Custom Django email backend using Resend Email API
    """

    def send_messages(self, email_messages):
        if not email_messages:
            return 0

        sent_count = 0
        for message in email_messages:
            response = requests.post(
                "https://api.resend.com/emails",
                headers={
                    "Authorization": f"Bearer {settings.RESEND_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "from": f"{settings.RESEND_SENDER_NAME} <{settings.DEFAULT_FROM_EMAIL}>",
                    "to": list(message.to),
                    "subject": message.subject,
                    "text": message.body,
                }
            )
            if response.status_code in [200, 202]:
                sent_count += 1
            else:
                if self.fail_silently is False:
                    raise Exception(f"Resend error: {response.status_code} - {response.text}")

        return sent_count
