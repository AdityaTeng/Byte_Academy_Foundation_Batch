# controller_weather.py
import view_weather
import model_weather

def GetChoice():
	choice=input(view_weather.StartView())
	if choice=='q' or choice== 'Q':
		view_weather.EndView()
	elif choice=='n' or choice=='N':
		search=GetLocation()
	else:
		view_weather.InvalidEntry()
		GetChoice()

def GetLocation():
	location=input(view_weather.LocationView())
	search=model_weather.LocationSearch(location)
	if search[0]=='Success':
		view_weather.LocationSuccess([search[1],search[2]])
		weatherList=model_weather.WeatherDetails(search[1],search[2])

		dateList=list(set([item[0] for item in weatherList]))
		view_weather.GetDate(dateList)
		dateInput=int(input())
		if dateInput in range(len(dateList)):
			wDate=dateList[dateInput]
		else:
			view_weather.InvalidEntry()
			GetChoice()

		timeList=list(set([item[1] for item in weatherList]))
		view_weather.GetTime(timeList)
		timeInput=int(input())		
		if timeInput in range(len(timeList)):
			wTime=timeList[timeInput]
		else:
			view_weather.InvalidEntry()
			GetChoice()		

		for item in weatherList:
			if item[0]==wDate and item[1]==wTime:
				view_weather.ViewWeather(item)		
		
		k=input()
		if k=='Q' or k=='q':
			view_weather.EndView()
		else:
			GetChoice()
	else:
		view_weather.LocationFailed([search[0],search[1]])
		GetChoice()

if __name__== '__main__':
	GetChoice()	

