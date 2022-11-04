# import smtplib
#
# my_email = "pythontesakun@gmail.com"
# password = "testes123"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="ahmadilhamhabibi@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(year)
#
# date_of_birth = dt.datetime(year=1995, month=6, day=28, hour=17)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

MY_EMAIL = "pythontesakun@gmail.com"
MY_PASSWORD = "testes123"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)

    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n{quote}"
                            )


