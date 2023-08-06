import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# 크롬 드라이버 실행 파일이 어디있는지 위치 명시
# 지금은 같은 경로에 있기 때문에, ()안에 아무것도 명시하지 않아도 무방함
driver = webdriver.Chrome()
# 어떤 주소로 크롬 브라우저가 접속할건지 지정
driver.get('https://naver.com')
# #query라는 요소라 로딩되어 나타날때까지 최대 '10초'까지 대기(우리가 찾고자 하는 요소가 나타나면 바로 대기를 중단하고 다음 코드 실행)
# 로딩이 완료되기 전에 요소를 클릭하거나 글을 입력하면 오작동할 수 있으므로, 이를 방지하기 위함
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#query')))
# 검색창 요소 특정
search_imput = driver.find_element(By.CSS_SELECTOR, '#query')
search_imput.send_keys('운세') # 검색하도록 지시
# 검색 버튼 특정
search_button = driver.find_element(By.CSS_SELECTOR, '#search-btn')
search_button.click() # 클릭하도록 지시
# 현재 브라우저 상 HTML을 변수에 저장
html = driver.page_source
# 잠시 종료전에 멈추고 검색 잘됐는지 확인
time.sleep(10)
# 브라우저 종료
driver.quit()

# 이제 bs4로 해당 html을 파싱
soup = BeautifulSoup(html, 'html.parser')
# a태그만 다 가져오기
a_elements = soup.select('a')
print(a_elements)


