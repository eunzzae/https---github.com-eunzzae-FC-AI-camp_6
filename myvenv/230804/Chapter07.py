import speech_recognition as sr
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 인식을 위한 객체 생성
r = sr.Recognizer()

# 마이크 사용을 위한 객체 생성
mic = sr.Microphone()
with mic as source: # 마이크에 담긴 소리를 토대로 아래 코드 실행
    print('인식 중...')
    audio = r.listen(source, timeout=5, phrase_time_limit=5) # 해당 소리를 오디오 파일 형태로 변환

try:
    result = r.recognize_google(audio, language = "ko-KR") # 오디오를 토대로 음성 인식
    print('결과: ' + result) # 인식 결과 출력
    # 인식이 됐으니 검색 시작 (지난 시간 selenium 부분 코드와 동일)
    driver = webdriver.Chrome()
    driver.get('https://naver.com')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#query')))
    search_input = driver.find_element(By.CSS_SELECTOR, '#query')
    search_input.send_keys(result)
    search_button = driver.find_element(By.CSS_SELECTOR, '#search-btn')
    search_button.click()
    time.sleep(10)
    driver.quit()
except sr.UnknownValueError:
    print("음성 인식 실패")
except sr.RequestError:
    print("서버 에러 발생")
except sr.WaitTimeoutError:
    print("인식 실패")