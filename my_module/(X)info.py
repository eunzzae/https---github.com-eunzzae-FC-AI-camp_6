# # 1. 네이버 검색 라이브러리
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup

# # 2. 날씨 알림 라이브러리
# import requests
# import json

# # 1. 네이버 검색 기능 구현
# # 크롬 드라이버 파일 경로 
# driver = webdriver.Chrome()
# # 네이버 크롬 브라우저에 접근할 것을 지정
# driver.get('https://naver.com')
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#query')))
# # 검색창 요소 특정
# search_input = driver.find_element(By.CSS_SELECTOR, '#query')
# # key 값을 지정해주는 명령어 등록해야함 *** 
# search_input.send_keys(f'{search_name}')
# #검색 버튼 특정
# search_button = driver.find_element(By.CSS_SELECTOR, '#search-btn')
# search_button.click()
# html = driver.page_source
# driver.quit()

# soup = BeautifulSoup(html, 'html.parser')
# a_elements = soup.select('a')
# print(a_elements)

# # 2. 실시간 날씨 알림 기능 구현
# html = requests.get(f'https://search.naver.com/search.naver?query=영등포+날씨')
# # html
# soup = BeautifulSoup(html.text, 'html.parser')

# # 위치
# address = soup.find('div',{'class':'title_area _area_panel'}).find('h2',{'class':'title'}).text
# adress_speak = print("궁금하신 위치는 " + address + " 입니다.")

# # 날씨 정보
# weather_data1 = soup.find('div',{'class':'weather_info'})

# # 현재 온도
# temperature = weather_data1.find('div',{'class':'temperature_text'}).text.strip()[5:]
# temperature_speak = print(f"{address}의 온도는 {temperature} 입니다.")

# # 날씨 상태
# weather_Status = weather_data1.find('span',{'class':'weather before_slash'}).text
# weather_Status_speak = print(f"{address}의 날씨 상태는 {weather_Status} 입니다.")

# # 공기 
# air= soup.find('ul',{'class':'today_chart_list'})
# infos = air.find_all('li',{'class':'item_today'})
# # fine_dust = infos[0].find('',{'':''})
# # fine_ultra_dust = infos[0].find('',{'':''}) 
# # fine_ozone = infos[0].find('',{'':''})

# for info in infos:
#     info_speak = print(info.text.strip())

# # # 시간대별 날씨 정보
# # weather_Time = soup.find_all('li',{'class':'_li'})
# # for i in weather_Time:
# #     print(i.text.strip())
