import schedule
import csv
import time
import json
import requests


def getweather():

	url = "https://api.openweathermap.org/data/2.5/weather"

	querystring = {"lat":"12.97","lon":"77.59","appid":"6d24a38de70af446667aa5ce084e6428"}

	headers = {
		'cache-control': "no-cache",
		'postman-token': "b5c037ed-c47b-2e94-5411-13e8d9d8f6ee"
		}

	response = requests.request("GET", url, headers=headers, params=querystring)

	#print(response.text)


	y = response.text

	z = json.loads(y)

	return z



def epochtime():
    current_time  = time.time()
    return current_time

def temp(z):
    t = round(z['main']['temp']-273,2)
    return t

def humidity(z):
    h = z['main']['humidity']
    return h

def lat(z):
    l= z['coord']['lat']
    return l

def long(z):
    lo= z['coord']['lon']
    return lo

def city(z):
    c = z['name']
    return c


def writedata():
	input_data = getweather()
	c_t = epochtime()
	t = temp(input_data)
	hum = humidity(input_data)
	la = lat(input_data)
	lo = long(input_data)
	c = city(input_data)
	print(c_t, t, hum, la, lo, c)
	fields = [c_t, t, hum, la, lo, c]
	#fields = ["epochtime", "temp", "hum","lat", "long", "city"]

	filename = "weatherdata.csv"
	with open(filename, 'a') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(fields) 



schedule.every(5).seconds.do(writedata)


while True:


    schedule.run_pending()
    time.sleep(1)








