import requests
import PySimpleGUI as sg

sg.theme('DarkBlue6')


sg.set_options(font='verdana 15')

layout = [
    [sg.Text('Weather Condition')],
    [sg.InputText(key='-CITY-', size=15), sg.Button('Go')],
    [ sg.Text('Country:'),sg.Text(key='-COUNTRY-', size=15), sg.Push(), sg.Text('Local Time:'), sg.Text(key='-TIME-', size=15)],
    [ sg.Text('Weather Now:'),sg.Text(key='-WEATHER-', size=15),  sg.Push(), sg.Text('Feels Like:'), sg.Text(key='-FEELS_LIKE-', size=15)],
    [sg.Text('Condition:'),sg.Text(key='-CONDITION-', size=15),  sg.Push(), sg.Text('Rain Chance:'), sg.Text(key='-RAIN-', size=15)],
    [sg.Text('Max:'),sg.Text(key='-MAX-', size=15),  sg.Push(), sg.Text('Min:'), sg.Text(key='-MIN-', size=15)]
]
window = sg.Window('Weather Condition', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Go':

        city = values['-CITY-']
        url = f"https://api.weatherapi.com/v1/forecast.json?key=9995875e61004c15be2171954232806&q={city}&days=1&aqi=no&alerts=no#"

        res = requests.get(url)
        res = res.json()

        city = res['location']['name']
        country = res['location']['country']
        localtime = res['location']['localtime']

        weather_now = res['current']['temp_c']
        feels_like = res['current']['feelslike_c']
        condition_now = res['current']['condition']['text']
        src_icon = res['current']['condition']['icon']

        forecast_max = res['forecast']['forecastday'][0]['day']['maxtemp_c']
        forecast_min = res['forecast']['forecastday'][0]['day']['mintemp_c']
        forecast_rain = res['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
        forcast_snow = res['forecast']['forecastday'][0]['day']['daily_chance_of_snow']
        forecast_icon = res['forecast']['forecastday'][0]['day']['condition']['icon']

        window['-COUNTRY-'].update(country)
        window['-TIME-'].update(localtime)
        window['-WEATHER-'].update(weather_now)
        window['-FEELS_LIKE-'].update(feels_like)
        window['-CONDITION-'].update(condition_now)
        window['-CONDITION-'].update(condition_now)
        window['-RAIN-'].update(forecast_rain)
        window['-MAX-'].update(forecast_max)
        window['-MIN-'].update(forecast_min)



window.close()
