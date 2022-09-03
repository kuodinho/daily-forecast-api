import requests
import json
import sys
from datetime import date
today = date.today()
def engine():
    data = json.dumps(response.json(), indent=4)
    jsn = json.loads(data)
    
    all_info = jsn['DailyForecasts']
    daily = all_info[0]
    
    temp = daily['Temperature']
    min = temp["Minimum"]
    max = temp["Maximum"]
    min_value = min["Value"]
    max_value = max["Value"]
    print("Max. temp. in F: ", max_value, "Min. temp. in F: ", min_value)
    
    min_value_c = (min["Value"]-32)/2
    max_value_c = (max["Value"]-32)/2
    print("Max. temp. in C: ", max_value_c, "Min. temp. in C: ", min_value_c)
    
    clouds = daily['Day']
    clouds2=clouds['IconPhrase']
    print("Clouds?", clouds2)
    rain = clouds['HasPrecipitation']
    print("Is it rain today?", rain)
    if str(rain) == 'False':
        print("Yay! U can ride a bike!")
    else:
        print("comunications")

def whatwear():
    x = input("Hello sunshine! Wanna know daily forecasts in WWa? (y/n)")
    if x == "y":
        print("Today is: ", today)
        engine()

    elif x == "n":
        print("Cool, have a nice day")
        sys.exit(0)
    else:
        print("Wrong letter, try again")

response = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/274663?apikey=9Kd9RdhI6V9AGV15DZa92WDCGjdUxkfz%20')
if (response.status_code != requests.codes.ok):
    print("coś jest nie teges")
else:
    whatwear()
   
