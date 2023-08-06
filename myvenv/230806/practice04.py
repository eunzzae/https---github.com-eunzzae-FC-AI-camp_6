import requests
import json

cities = [{'name':'Seoul', 'latitude' : 37.566, 'longitude' :126.9784},
          {'name':'Sydney', 'latitude' : -33.8678, 'longitude' :151.2073},
          {'name':'London', 'latitude' : 51.5085, 'longitude' :-0.1257}]

def get_weather(latitude, longitude):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&current_weather=true'
    
    response = requests.get(url)
    json_data = json.loads(response.text)
    print(f"{json_data['current_weather']['temperature']}도")

for city in cities:
    print(f"{city['name']}의 날씨")
    get_weather(city['latitude'], city['longitude'])