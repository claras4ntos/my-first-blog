import csv
import smtplib
from settings import SENDER_EMAIL, SENDER_PASSWORT


ACCEPTED_MSG = """
HI {}

blablabla

Your coach is {}.

blablabla
"""

REJECTED_MSG = """
Hi {}

blablabla

"""


with open('applications.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    smtp = smtplib.SMTP('smtp.gmail.com')
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(SENDER_EMAIL, SENDER_PASSWORT)
    for row in csv_reader:
        name, email, accepted, coach, language = row

        if accepted == "YES":
            msg = ACCEPTED_MSG.format(name, coach)
            subject = "Workshop Application - Accepted"
        else:
            msg = REJECTED_MSG.format(name)
            subject = "Workshop Application - Denied"

        email_msg = "Subject: {} \n\n{}".format(subject, msg)
        smtp.sendmail(SENDER_EMAIL, email, email_msg)

    smtp.quit
