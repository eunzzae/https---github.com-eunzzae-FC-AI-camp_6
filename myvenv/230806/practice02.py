# 멜론 월별 1-50위 순위 가져오기 

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
driver.get('https://www.melon.com/chart/month/index.htm')
# 월 선택 부분 클릭
month_selector = driver.find_element(By.CSS_SELECTOR, '#conts > div.calendar_prid > div > button')
month_selector.click()

music_list = [['제목', '가수']]
# 특정 월을 클릭하고 곡 데이터를 출력하는 부분은 각 월마다 반복
for i in range(1,7) : # 1~6까지 반복
    # 특정 월 클릭
    month_element = driver.find_element(By.CSS_SELECTOR, f'#conts > div.calendar_prid > div > div > dl > dd.month_calendar > ul > li:nth-child({i}) > a > span')
    month_element.click()
    # 잘 클릭됐는지 확인하기 위해 잠깐 슬립
    time.sleep(1)

    # 현재 html을 변수로 저장
    html = driver.page_source
    # 파싱하기
    soup = BeautifulSoup(html, 'html.parser')
    # 원하는 정보 선택
    titles = soup.select('.lst50 .rank01 a')
    artists = soup.select('.lst50 .rank02 > a')
    
    for i in range(50):
        print(f'[{i}] : {titles[i].text}-{artists[i].text}')

# 드라이버 종료
driver.quit()