# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:55:03 2021

@author: 91905
"""

import requests
from datetime import datetime

api_key='163f3b16a4b8031bce974adb5e767a7d'
location = input('Enter name of the place: ')

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city=((api_data['main']['temp'])-273.15)
weather_desc=api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

print("====================================================")


txtlist = [temp_city,weather_desc,hmdt,wind_spd,date_time]

