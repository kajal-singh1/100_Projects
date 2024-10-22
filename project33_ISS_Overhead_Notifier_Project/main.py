import requests
from datetime import timedelta,datetime
from dateutil import parser
import smtplib
import time

MY_LAT = 17.387140
MY_LONG = 78.491684
MY_EMAIL = "riyasolankhi9@gmail.com"
PASSWORD = "qlfc sufc diro bfqy"
IST_OFFSET = timedelta(hours=5, minutes=30)

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (longitude, latitude)

    if (MY_LAT - 5 <= latitude <= MY_LAT + 5) and \
    (MY_LONG - 5 <= longitude <= MY_LONG + 5):
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0 
    }

    response = requests.get(url = "https://api.sunrise-sunset.org/json", params= parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    sunrise_time_utc = parser.parse(sunrise)
    sunset_time_utc = parser.parse(sunset)
    sunrise_time_ist = (sunrise_time_utc + IST_OFFSET).time().hour
    sunset_time_ist = (sunset_time_utc + IST_OFFSET).time().hour

    time_now = datetime.now().hour

    if time_now >= sunset_time_ist or time_now <= sunrise_time_ist:
        return True
    
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs= MY_EMAIL,
            msg="Subject:Look Up👆 \n\n The ISS is above you in the sky "
        )
    print("email sent")

