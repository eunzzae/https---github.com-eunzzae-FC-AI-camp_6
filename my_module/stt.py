import speech_recognition as sr
from tts import speak
# tts.py 에 작성한 speak 함수 불러오기

# 인식을 위한 객체 생성
def listen():
    r = sr.Recognizer()

    # 마이크 사용을 위한 객체 생성
    mic = sr.Microphone()
    with mic as source: # 마이크에 담긴 소리를 토대로 아래 코드 실행
        print('인식 중...')
        audio = r.listen(source, timeout=5, phrase_time_limit=5) # 해당 소리를 오디오 파일 형태로 변환

    try:
        result = r.recognize_google(audio, language = "ko-KR") # 오디오를 토대로 음성 인식
        print('결과: ' + result) # 인식 결과 출력
        if result == '안녕': # 안녕이라고 말했으면
            speak('안녕하세요') # 컴퓨터가 안녕하세요라고 응답
    except sr.UnknownValueError:
        print("음성 인식 실패")
    except sr.RequestError:
        print("서버 에러 발생")
    except sr.WaitTimeoutError:
        print("인식 실패")

if __name__ == "__main__":
    listen()