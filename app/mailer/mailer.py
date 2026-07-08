from app.extensions import mail
from flask_mail import Message
class Mailer:
    def sendNotificationEmail(to,subject, body):
        msg = Message(
        subject=subject,
        recipients=[to],
        body=body
        )
        # current_app.logger.info("mail sending...")
        mail.send(msg)
        