import smtplib
import datetime as dt 
import random

now = dt.datetime.now()
current_day = now.weekday()
if current_day == 0:
#opening Text File
    with open("100_Projects/project32_Birthday_Email/quotes.txt") as quote:
        file_content = quote.readlines()
        random_quote = random.choice(file_content)
        # print(random_quote)

    my_email = "riya9@gmail.com"
    password = "qlfc sufc diro bfqy"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n {random_quote}"
            )
    
print("Email sent")

