import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# 크롬 드라이버 실행 파일이 어디있는지 위치 명시
# 지금은 같은 경로에 있기 때문에, () 안에 아무것도 명시하지 않아도 무방
driver = webdriver.Chrome()
# 어떤 주소로 크롬 브라우저가 접속할 건지 지정
driver.get('https://naver.com')
# 검색창이 로딩되어서 나타날때까지 최대 '10초'까지 대기 (우리가 찾고자 하는 요소가 나타나면 바로 대기를 중단하고 다음 코드 실행)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#query')))
# 검색창 요소 특정
search_input = driver.find_element(By.CSS_SELECTOR, '#query')
search_input.send_keys('안녕하세요') # 검색하도록 지시
# 검색 버튼 특정
search_button = driver.find_element(By.CSS_SELECTOR, '#search-btn')
search_button.click() # 클릭하도록 지시
# 현재 브라우저 상의 HTML을 변수에 저장
# time.sleep() 등으로 검색이 끝날때까지 기다린 후에 해당 페이지 html 을 저장하는 것이 더욱 정확함
html = driver.page_source
# 브라우저 종료
driver.quit()

# 이제 bs4로 해당 html을 파싱
soup = BeautifulSoup(html, 'html.parser')
tag = soup.select('.mean')
print(tag[1].text)


# 지난 시간 크롤링
# 1. requests 모듈을 써서 웹 주소에 요청을 보내고, 응답으로 HTML을 받아옴
# 2. 그 HTML을 beaurifulsoup 모듈을 써서 파싱(문자열 -> HTML구조)
# 3. 파싱된 데이터를 토대로 우리가 원하는 정보가 있는 태그를 명시해서 추출

