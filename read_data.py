import csv

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

    for row in csv_reader:
        name, email, accepted, coach, language = row

        if accepted == "YES":
            msg = ACCEPTED_MSG.format(name, coach)
        else:
            msg = REJECTED_MSG.format(name)

        print("Send e-mail to: {}".formt(email))
        print("E-mail content:")
        print(msg)
