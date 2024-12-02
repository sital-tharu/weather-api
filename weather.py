import json
import requests
city_name=input('Enter a city Name:')
api_key='2c0c2746adaec43b0a00589692820720'

api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
get_server_information=requests.get(api_url)
print(get_server_information.json())
