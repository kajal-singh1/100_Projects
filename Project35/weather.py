import requests

URL = 'http://api.openweathermap.org/data/2.5/weather'
API_KEY = 'f328c0db7540fb32a57904e3f147c240'

parameters = {
    'q': 'Tokyo',  # Use a city name for testing
    'appid': API_KEY
}

try:
    response = requests.get(url=URL, params=parameters)
    response.raise_for_status()  # Check for HTTP errors
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")
    if response:
        print("Response Content:", response.content)  # Show error details
