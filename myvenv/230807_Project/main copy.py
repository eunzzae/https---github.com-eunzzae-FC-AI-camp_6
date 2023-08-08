import speech_recognition as sr
from tts import speak

r = sr.Recognizer()

while True:
    with sr.Microphone() as source: # 마이크에 담긴 소리를 토대로 아래 코드 실행
        print('인식 중...')
        audio = r.listen(source, timeout=7, phrase_time_limit=5)
        result = r.recognize_google(audio, language = "ko-KR")
        if "지니" in result or "지니야" in result or "지미" in result:
            print(result)
            speak("네")
        else:
            try:
                if result == '안녕'in result or "안영" in result or "안녕안녕" in result: 
                    speak('안녕하세요') 
                elif result == '검색'in result or "검색해줘" in result or "검색해" in result:
                    speak('네이버에 검색합니다.')
                elif result == '날씨'in result or "날씨알려줘" in result:
                    speak('오늘의 날씨는')
                elif result == '미세먼지'in result or "공기 어때" in result or "오늘 공기" in result:
                    speak('오늘의 미세먼지는 ')
            except sr.UnknownValueError:
                speak("이해하지 못하는 말이에요")
            except sr.RequestError:
                speak("서버 에러 발생")
            except sr.WaitTimeoutError:
                speak("인식 실패")
