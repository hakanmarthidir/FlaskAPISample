from threading import Thread
from flask import Flask
from flask_mail import Message, Mail
import config

app = Flask(__name__)

# NOTICE :
# 1- Open -> Google Account Setting Page on Your Sender Account
# 2- Signing Into Google
# 3- Allow less secure apps -> OK


mail_settings = {
    "MAIL_SERVER": config.Config.MailServer,
    "MAIL_PORT": config.Config.MailPort,
    "MAIL_USE_TLS": config.Config.MailUseTls,
    "MAIL_USE_SSL": config.Config.MailUseSsl,
    "MAIL_USERNAME": config.Config.MailUserName,
    "MAIL_PASSWORD": config.Config.MailUserPass
}

app.config.update(mail_settings)
mail = Mail(app)


def sendemail():
    with app.app_context():
        msg = Message(subject="Hello", sender=config.Config.MailUserName, recipients=["toaddress"],
                      body="Flask Mail")
        mail.send(msg)
        print('sent')


def sendasync(app, msg):
    with app.app_context():
        mail.send(msg)


def asyncemail(app):
    with app.app_context():
        msg = Message(subject="Hello", sender=config.Config.MailUserName, recipients=["toaddress"],
                      body="Flask Mail")
        thr = Thread(target=sendasync, args=[app, msg])
        thr.start()
        return thr


asyncemail(app)
print('Sent')
