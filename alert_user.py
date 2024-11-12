import yagmail
from creds import google_email, google_password, reciever2_email, reciever_email

def alert_user():
    yag = yagmail.SMTP(google_email, google_password)
    yag.send(reciever_email, 'GET HYPE', 'NEW ASSIGNMENT OR GRADE DROPPED')
    yag.send(reciever2_email, 'GET HYPE', 'NEW ASSIGNMENT OR GRADE DROPPED')
