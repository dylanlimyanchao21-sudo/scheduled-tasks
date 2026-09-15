##################### Hard Starting Project ######################
import os
import smtplib
import datetime as dt
import random as r
import pandas as pd

#login details
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

# datetime now info
now = dt.datetime.now()
today_tuple = (now.month, now.day)

df = pd.read_csv("birthdays.csv")
birthdays_dict = df.set_index(['month', 'day']).to_dict('index')
if today_tuple in birthdays_dict:
    file_path = f"letter_templates/letter_{r.randint(1,3)}.txt"
    birthday_person = birthdays_dict[(today_tuple)]

    with open(file_path) as f:
        letter = f.read()

    letter = letter.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject: Happy Birthday!\n\n{letter}")

