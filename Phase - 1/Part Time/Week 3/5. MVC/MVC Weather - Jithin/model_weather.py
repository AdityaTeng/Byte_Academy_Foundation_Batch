# model_weather.py
import json
import requests
import datetime

def LocationSearch(location):
	with open("city.list.json","r", encoding="utf8") as cityJSON:
		data=json.load(cityJSON)

	for item in data:
		if item['name']==location:
			return ['Success',item['name'],item['country']]
	return ['Failed',location]
	
# location,country
def WeatherTime(dt):
	dtItem=datetime.datetime.fromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')
	dtList=dtItem.split(' ')
	return dtList

def WeatherDetails(location,country):

	url='http://api.openweathermap.org/data/2.5/forecast?q='+location+','+country+'&units=imperial&APPID=1960401d79b51d8c3be286b9463a081b'
	source=requests.get(url)
	weather=json.loads(source.text)
	weatherList=[]
	#weatherlsit = [Time,City,Temp,MinTemp,MaxTemp,Wind,Cloud,Humidity]
	for weatherItem in weather['list']:
		weatherList.append([WeatherTime(weatherItem['dt'])[0],WeatherTime(weatherItem['dt'])[1],location,country,weatherItem['main']['temp'],weatherItem['main']['temp_min'],weatherItem['main']['temp_max'],weatherItem['wind']['speed'],weatherItem['clouds']['all'],weatherItem['main']['humidity']])
	return weatherList



location='Bangalore'
country='IN'
WeatherDetails(location,country)


