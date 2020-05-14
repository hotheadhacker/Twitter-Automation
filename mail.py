# smtplib module send mail

import smtplib
import config

TO = 'annonymous@hi2.in'
SUBJECT = 'Trends For Kashmir'
TEXT = 'Here is a message from python.'

# Gmail Sign In
gmail_sender = 'kmrtrends@gmail.com'
gmail_passwd = config.password

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print('email sent')
except:
    print('error sending mail')

server.quit()
