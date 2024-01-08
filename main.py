import requests
from datetime import datetime

USERNAME = "nhatek"
TOKEN = "PQ88wP1grYE2"
GRAPH_ID = "reading1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": TOKEN
}

# 1. CREATE A USER PROFILE AND PRINT RESULT IN CONSOLE

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


# 2. CREATE A NEW GRAPH AND PRINT RESULT IN CONSOLE

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading",
    "unit": "pages",
    "type": "int",
    "color": "ajisai",
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)


# 3. POST A PIXEL AND PRINT RESULT IN CONSOLE

"""
today = datetime(year=2024, month=1, day=7)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "12",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
"""

# 4. UPDATE A PIXEL AND PRINT RESULT IN CONSOLE

"""
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{datetime.today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "0"
}

response = requests.post(url=pixela_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

"""
