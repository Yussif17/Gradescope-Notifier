import yagmail
from creds import google_email, google_password

def alert_user():
    yag = yagmail.SMTP(google_email, google_password)
    yag.send('yussiframa10@gmail.com', 'Hello sir', 'Good day')
    print("Email sent successfully!")