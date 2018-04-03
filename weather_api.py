# import requests
#
# package = {
#     'APPID': '7b7d314d8287da1381d647db8c51d4c2',
#     'q': 'portland'
#     }
#
# r = requests.post(
#     'https://api.openweathermap.org/data/2.5/weather', params=package)
# data = r.json()
# print(data)

import requests

city = input("Enter City: ")
payload = {
    'APPID': '7b7d314d8287da1381d647db8c51d4c2',
    'q': city
}

r = requests.post(
    'https://api.openweathermap.org/data/2.5/weather?', params=payload
    )
data = r.json()
tempf = data['main']['temp'] * (9 / 5) - 459.67
tempc = data['main']['temp'] - 273
print(r.url)
print("Farenheit:\t", tempf)
print("Celcius:\t", tempc)
