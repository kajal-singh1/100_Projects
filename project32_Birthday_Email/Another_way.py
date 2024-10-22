import smtplib  
import datetime as dt  
import random  
import pandas  as pd

MY_EMAIL = "riya9@gmail.com"
MY_PASSWORD = "qlfc sufc diro bfqy"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("100_Projects/project32_Birthday_Email/birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]):data_row for  (index, data_row) in data.iterrows() }
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"100_Projects/project32_Birthday_Email/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr= MY_EMAIL, to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!! \n\n {contents}")
        
print("Email Sent")
