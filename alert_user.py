import yagmail
from creds import google_email, google_password, reciever2_email, reciever_email

def alert_user(message):
    yag = yagmail.SMTP(google_email, google_password)
    yag.send(reciever_email, 'GET HYPE', message)
    yag.send(reciever2_email, 'GET HYPE', message)
