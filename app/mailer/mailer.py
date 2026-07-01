from app.extensions import mail
from flask_mail import Message
# from flask import current_app
class Mailer:
    def sendNotificationEmail(to,subject, body):
        msg = Message(
        subject=subject,
        recipients=[to],
        body=body
        )
        # current_app.logger.info("mail sending...")
        mail.send(msg)
        