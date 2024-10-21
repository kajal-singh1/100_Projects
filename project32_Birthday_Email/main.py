import smtplib
import datetime as dt 
import random
import pandas

now = dt.datetime.now()
current_month = now.month
current_day = now.weekday()
birthday = (current_month, current_day)
# print(current_month)
# print(current_day)
# print(birthday)

data = pandas.read_csv("100_Projects/project32_Birthday_Email/birthdays.csv")
