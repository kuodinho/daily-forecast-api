import requests
import json
import sys
from datetime import date
today = date.today()
def engine():
    data = json.dumps(response.json(), indent=4)
    jsn_object = json.loads(data)
    y = jsn_object['DailyForecasts']
    nest_dict = y[0]
    temp = nest_dict['Temperature']
    min = temp["Minimum"]
    max = temp["Maximum"]
    min_value = min["Value"]
    max_value = max["Value"]
    print("Max. temp. in F: ", max_value, "Min. temp. in F: ", min_value)
    min_value_c = (min["Value"]-32)/2
    max_value_c = (max["Value"]-32)/2
    print("Max. temp.: ", max_value_c, "Min. temp.: ", min_value_c)
    clouds = nest_dict['Day']
    rain = clouds['HasPrecipitation']
        
    print("Is it rain today?", rain)
    if str(rain) == 'False':
        print("U can ride a bike")
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
        #data = json.dumps(response.json(), indent=4) #idziemy do konsoli; json.dumps() function converts a Python object into a json string
        #jsn_object = json.loads(data) #can be used to parse a valid JSON string and convert it into a Python Dictionary
    #print(type(jsn_object))
    #print(jsn_object.keys())
        #y = jsn_object['DailyForecasts']
    #print(y)
    #print(type(y))
    #print(len(y))
        #nest_dict = y[0]
    #print(nest_dict)
    #print(type(nest_dict))
        #temp = nest_dict['Temperature']
    #print(temp)
    #min = temp["Minimum"]
    #max = temp["Maximum"]
    #min_value = min["Value"]
    #max_value = max["Value"]
    #print("Max. temp. in F: ", max_value, "Min. temp. in F: ", min_value)
    #min_value_c = (min["Value"]-32)/2
    #max_value_c = (max["Value"]-32)/2
    #print("Max. temp.: ", max_value_c, "Min. temp.: ", min_value_c)
    #clouds = nest_dict['Day']
    #rain = clouds['HasPrecipitation']
    #print("Is it rain today?", rain)
   
   
   
   
   
   
   # print(json.dumps(response.json(), indent=4))
   # print(response.getJSONArray("Temperature"))
    #data = json.dumps(response.json(), indent=4) #idziemy do konsoli; json.dumps() function converts a Python object into a json string
    #jsn_object = json.loads(data)
   # print(type(jsn_object))
    #print(jsn_object.keys())
    #print(jsn_object['DailyForecasts'])/
    #DailyForecasts["Temperature"])
    #def whatwear():
    #user_choice = input("What do you want to know?(temp./rain)")
    #if user_choice == "temp":
        #print(data.Temperature)
    #elif user_choice == "rain":
        #print(json.PrecipitationType[0])  
