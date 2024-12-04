import json
import requests
from dotenv import load_dotenv
import os 
load_dotenv()
city_name=input('Enter a city Name:')
api_key=os.getenv('api_key')

api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
get_server_information=requests.get(api_url)
data=get_server_information.json()
print(data)
pretty_data=json.dumps(data,indent=4)
print(pretty_data)

D = data["weather"][0]["description"]
T = data["main"]["temp"]

print(f'The Current Weather Description is :{D} & Temp. is :{T}')



