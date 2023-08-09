from bs4 import BeautifulSoup
import requests
import json

# 실시간 날씨 알림 기능 구현
# def weather_add(location):
#     html = requests.get(f'https://search.naver.com/search.naver?query={location}+날씨')
#     # html
#     soup = BeautifulSoup(html.text, 'html.parser')

#     # 위치
#     address = soup.find('div',{'class':'title_area _area_panel'}).find('h2',{'class':'title'}).text
#     adress_speak = print("궁금하신 위치는 " + address + " 입니다.")

    # html = requests.get(f'https://search.naver.com/search.naver?query={location}+날씨')
    # # html
    # soup = BeautifulSoup(html.text, 'html.parser')
    # # 날씨 정보
    # weather_data1 = soup.find('div',{'class':'weather_info'})

# 1.기온 정보
def weather_temp(location):
    html = requests.get(f'https://search.naver.com/search.naver?query={location}+날씨')
    # html
    soup = BeautifulSoup(html.text, 'html.parser')
    # 날씨 정보
    weather_data1 = soup.find('div',{'class':'weather_info'})
    address = soup.find('div',{'class':'title_area _area_panel'}).find('h2',{'class':'title'}).text
    # 현재 온도
    temperature = weather_data1.find('div',{'class':'temperature_text'}).text.strip()[5:]
    print(f"{address}의 온도는 {temperature} 입니다.")

# 2.날씨 상태   
def weather_sta(location):
    html = requests.get(f'https://search.naver.com/search.naver?query={location}+날씨')
    # html
    soup = BeautifulSoup(html.text, 'html.parser')
    # 날씨 정보
    weather_data1 = soup.find('div',{'class':'weather_info'})
    address = soup.find('div',{'class':'title_area _area_panel'}).find('h2',{'class':'title'}).text
    
    # 날씨 상태
    weather_Status = weather_data1.find('span',{'class':'weather before_slash'}).text
    print(f"{address}의 날씨 상태는 {weather_Status} 입니다.")

# 3.대기 상태   
def weather_air(location):
    html = requests.get(f'https://search.naver.com/search.naver?query={location}+날씨')
    # html
    soup = BeautifulSoup(html.text, 'html.parser')
    # 날씨 정보
    weather_data1 = soup.find('div',{'class':'weather_info'})
    address = soup.find('div',{'class':'title_area _area_panel'}).find('h2',{'class':'title'}).text
    # 공기 
    air= soup.find('ul',{'class':'today_chart_list'})
    infos = air.find_all('li',{'class':'item_today'})
    for info in infos:
        print(info.text.strip())

if __name__ == "__main__":
    location = input('입력 : ')
    weather_temp(location)
    weather_sta(location)
    weather_air(location)
    
    



# def weather_func(location):
#     html = requests.get(f'https://search.naver.com/search.naver?query={location}+날씨')
#     # html
#     soup = BeautifulSoup(html.text, 'html.parser')

#     # 위치
#     address = soup.find('div',{'class':'title_area _area_panel'}).find('h2',{'class':'title'}).text
#     adress_speak = print("궁금하신 위치는 " + address + " 입니다.")

#     # 날씨 정보
#     weather_data1 = soup.find('div',{'class':'weather_info'})

#     # 현재 온도
#     temperature = weather_data1.find('div',{'class':'temperature_text'}).text.strip()[5:]
#     temperature_speak = print(f"{address}의 온도는 {temperature} 입니다.")

#     # 날씨 상태
#     weather_Status = weather_data1.find('span',{'class':'weather before_slash'}).text
#     weather_Status_speak = print(f"{address}의 날씨 상태는 {weather_Status} 입니다.")

#     # 공기 
#     air= soup.find('ul',{'class':'today_chart_list'})
#     infos = air.find_all('li',{'class':'item_today'})

#     for info in infos:
#         info_speak = print(info.text.strip())