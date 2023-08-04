# API = 매개체

# 식당 = 주문
# 주문하기 위한 매개체 = 메뉴판/키오스크
# 고객 - 키오스크로 주문
# 키오스크 -> 주방에다가 전달(누가 ~ 주문했어)
# 주방 - 고객한테 요리를 전달

# 날씨 정보를 보여주는 웹/앱서비스
# 날씨를 직접 측정하는 애들은 기상청/관측소
# 기상청이 가진 데이터를 가져와서 프로그램을 만들어야 함
# 개발자 - 날씨 API에다가 '날씨 정보 좀 줘' 요청(request)
# 날씨 API(웹 서버) 기상청 데이터를 가지고 옴, 우리한테 전달
# 기상청 DB - 날씨 API 한테만 데이터 전달

import requests
import json

cities = [{'name':'Seoul', 'latitude' : 37.56, 'longitude' : 126.97},
          {'name': 'London', 'latitude': 51.50, 'longitude': -0.12},
        {'name': 'New York', 'latitude': 40.71, 'longitude': -74.00}]

def get_weather(latitude, longitude):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'

    response = requests.get(url)
    data = json.loads(response.text)
    print(f"{data['current_weather']['temperature']}도")  #문자열에 불과 -> 파이썬 상의 딕셔너리/리스트

for city in cities:
    print(f"{city['name']}의 날씨")
    get_weather(city['latitude'],city['longitude'])

