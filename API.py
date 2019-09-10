import requests
import pprint
import datetime

def get_lat_long(place=None):
	query_url = (
		"https://api.weather.com/v3/location/search"
		"?apiKey=d522aa97197fd864d36b418f39ebb323"
		"&format=json"
		"&language=en-IN"
		"&locationType=locale"
		"&query="
		)
	query_url = query_url+place
	print(("Get request at API endpoint : {0}")
		.format(query_url))
	r = requests.get(query_url)
	if r.status_code == 200:
		return r.json()
	else:
		return None

def selected_place_lat_long(loc_json,selection=0):
	print("Your selected Place is : " 
		+ loc_json["location"]["address"][selection])
	return(loc_json["location"]["latitude"][i]
		,loc_json["location"]["longitude"][i])

def get_daily_forecast(lat=0,lon=0):
	query_url = (
		"https://api.weather.com/v2/turbo/vt1observation"
		"?apiKey=d522aa97197fd864d36b418f39ebb323"
		"&format=json"
		"&geocode="
		+str(lat)+
		"%2C"
		+str(lon)+
		"&language=en-IN"
		"&units=m"
		)
	print(("Get request at API endpoint : {0}")
		.format(query_url))
	r = requests.get(query_url)
	if r.status_code == 200:
		return r.json()
	else:
		return None

if __name__ == '__main__':
	place = input("Enter Name of Place : ")
	received_locs = get_lat_long(place)
	num_received_locs = len(received_locs["location"]["address"])
	for i in range(num_received_locs):
		print(str(i+1)+"."
			+received_locs["location"]["address"][i])
	sel_loc = input("Select Your Preference : ")
	if ((sel_loc==None) or (sel_loc.isdigit()==False)):
		print("Incorrect input format! Selection set to 1")
		sel_loc = 0
	else:
		sel_loc = int(sel_loc)-1
	lat,lon=selected_place_lat_long(received_locs,sel_loc)
	print("Selected Place has latitude : "
		+str(lat)
		+" and logitude : "
		+str(lon))
	date_entry = input('Enter a date in YYYY-MM-DD format : ')
	year, month, day = map(int, date_entry.split('-'))
	date1 = datetime.date(year, month, day)
	print("Types of forecast : ")
	print("1. Daily")
	print("2. Monthly")
	type_of_forecast=input("Enter type of forecast : ")
	if type_of_forecast == "1":
		forecast = get_daily_forecast(lat,lon)
	pprint.pprint(forecast)


