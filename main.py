import datetime as dt
import random
import smtplib
import pandas
import os
from dotenv import load_dotenv
load_dotenv()
today = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
row = data.to_dict(orient="records")
email = os.getenv("email")
password = os.getenv("password")

for l in row:
    replace = [f"{l["name"]}", 2025 - l["year"]]
    receiver = l["email"]
    month = l["month"]
    day = l["day"]
    if month == today.month and day == today.day:
        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as f:
            g = f.read()
            g = g.replace("[NAME]", replace[0])
            g = g.replace("[YEAR]", f"{replace[1]}")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(email,password)
            connection.sendmail(from_addr=email,to_addrs=receiver,msg=f"Subject:Birthday Wishes\n\n{g}")


