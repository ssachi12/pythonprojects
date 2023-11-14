import time

import requests

def weather(city):
    appid = '89947360cc83ebc330589ab41fd78f44'

    URL = \
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={appid}'

    r = requests.get(URL)
    res = r.json()
    condition = res['weather'][0]['main']
    description = res['weather'][0]['description']
    temp = res['main']['temp']

    print("condition : ", condition)
    print("description : ", description)
    print("temprature : ", temp, "C")

city=input("enter the city")
while True:
    weather(city)
    time.sleep(5)
    print()