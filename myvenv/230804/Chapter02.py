import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# 크롬 드라이버 실행 파일이 어디있는지 위치 명시
# 지금은 같은 경로에 있기 때문에, () 안에 아무것도 명시하지 않아도 무방
driver = webdriver.Chrome()
driver.get('https://www.melon.com/chart/month/index.htm')
# 월 선택 부분 클릭 
month_selector = driver.find_element(By.CSS_SELECTOR, '#conts > div.calendar_prid > div > button') # 월 선택 버튼의 html문서를 복붙하기
month_selector.click()

# 특정 월을 클릭하고 곡 데이터를 출력하는 부분은 각 월마다 반복
for i in range(1, 7) : # 1~6까지 반복
    month_element = driver.find_element(By.CSS_SELECTOR, f'#conts > div.calendar_prid > div > div > dl > dd.month_calendar > ul > li:nth-child({i}) > a')
    month_element.click()
    
# 현재 html을 변수로 저장
    time.sleep(1)
    html=driver.page_source
# 파싱하기
    soup = BeautifulSoup(html, 'html.parser')    
# 원하는 정보 선택하기
    titles = soup.select('.lst50 .rank01 a')
    artists = soup.select('.lst50 .rank02 > a')
    for i in range(50):
        print(f'{titles[i].text}-{artists[i].text}')

# 드라이버 종로
driver.quit()