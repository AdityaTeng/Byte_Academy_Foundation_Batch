def StartView():
	print("---Welcome to Weather Forecast Engine---")
	print("[N] for New Search")
	print("[Q] for Quit")
	return "Enter your Choice :"
	

def EndView():
	print("Thank you for using the Weather Forecast Engine.\nHave a great day! :)")
	return

def InvalidEntry():
	print("\nInvalid Entry!\n")

def LocationView():
	return "Enter Location :"

def LocationSuccess(sList):
	print("Location indentified :",sList[0],sList[1])
	return

def LocationFailed(sList):
	print(sList[1],"not in database, status :",sList[0])
	return


def GetDate(dateList):
	print("We have weather available for below Dates, Let us know your Choice :")
	for i in range(len(dateList)):
		print('[',i,']:',dateList[i])
	return "_"

def GetTime(timeList):
	print("We have weather available for below timings, Let us know your Choice :")
	for i in range(len(timeList)):
		print('[',i,']:',timeList[i])
	return "_"

def ViewWeather(item):
	print("---Weather Forecast Details---")
	print("Date                :\t",item[0])
	print("Time                :\t",item[1])
	print("City                :\t",item[2])
	print("Country             :\t",item[3])
	print("Average Temperature :\t",item[4])
	print("Minimum Temperature :\t",item[5])
	print("Maximum Temperature :\t",item[6])
	print("Wind                :\t",item[7])
	print("Cloudiness          :\t",item[8])
	print("Humidity            :\t",item[9])
	print('---Press Q for exit\n---Any key for Menu')
	return "_"



		





