import requests
from datetime import datetime

USERNAME = 'username'
TOKEN = 'token'
ID =   "graph1" 

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : 'token',
    "username": 'username',
    "agreeTermsOfService": 'yes',
    "notMinor": 'yes',
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph" ,
    "unit": "Hour" ,
    "type":"float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

today = datetime.now()

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
post_config = {
    "date": today.strftime('%Y%m%d'),
    "quantity" : input("How many hours do you coded today?"),
}

response = requests.post(url =post_endpoint, json=post_config, headers=headers)
print(response.text)

put_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today.strftime('%Y%m%d')}"
put_config = {
    "quantity" : '8.5',
}

response = requests.put(url = put_endpoint, json=put_config, headers=headers)
print(response.text)

del_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url = del_endpoint, headers=headers)
print(response.text)
