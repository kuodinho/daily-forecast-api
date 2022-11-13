import requests
import json
import sys
from datetime import date

def main():
    api_response = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/2day/274663?apikey=9Kd9RdhI6V9AGV15DZa92WDCGjdUxkfz%20')
    if (api_response.status_code != requests.codes.ok): 
        print("something wrong with response. Reason:", api_response.status_code, api_response.reason)
    else:
        users_answer = input("Hello sunshine! Wanna know daily forecasts in WWa? (y/n)")
        react_to_user_answer(api_response, users_answer)

def react_to_user_answer(api_response, users_answer):
    if users_answer == "y":
        print("Today is: ", date.today())
        print(daily_forecast(api_response))
    elif users_answer == "n":
        print("Cool, have a nice day")
        sys.exit(0)
    else:
        print("Wrong letter, try again")

def daily_forecast(api_response):
    serialized_api_response = json.dumps(api_response.json(), indent=4)
    api_response_to_object = json.loads(serialized_api_response)
    daily = api_response_to_object['DailyForecasts'][0]
    min_value = daily['Temperature']["Minimum"]["Value"]
    max_value = daily['Temperature']["Maximum"]["Value"]
    min_value_c = (min_value-32)/2
    max_value_c = (max_value-32)/2
    
    clouds=daily['Day']['IconPhrase']
    if str(clouds) == 'Showers':
        clouds_rain = "Yes, a lot"
    else:
        clouds_rain = clouds
   
    rain = daily['Day']['HasPrecipitation']
    if str(rain) == 'False':
        bike = "Yay! U can ride a bike!"
    else:
        bike = "- go by train"
    x = f'Max. temp. in F: {max_value} Min. temp. in F: {min_value}\nMax. temp. in C: {max_value_c}, Min. temp. in C: {min_value_c}\nIs it cloudy today?: {clouds_rain}\nIs it rain today?: {rain} {bike}'
    return x

if __name__ == '__main__':
    main()
    