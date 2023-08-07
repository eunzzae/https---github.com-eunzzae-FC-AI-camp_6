import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. 네이버 검색 기능 구현
# 크롬 드라이버 파일 경로 
driver = webdriver.Chrome()
# 네이버 크롬 브라우저에 접근할 것을 지정
driver.get('https://naver.com')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#query')))
# 검색창 요소 특정
search_input = driver.find_element(By.CSS_SELECTOR, '#query')
search_input.send_keys('{search_name}')
#검색 버튼 특정
search_button = driver.find_element(By.CSS_SELECTOR, '#search-btn')
search_button.click()
time.sleep(10)
driver.quit()

# 2. 실시간 날씨 알림 기능 구현






# 3. 미세먼지 알림 기능 구현