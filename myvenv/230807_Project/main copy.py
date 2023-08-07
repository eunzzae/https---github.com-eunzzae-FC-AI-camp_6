from gtts import gTTS 
import playsound
import os

def speak(text): 
	tts = gTTS(text=text, lang='ko') 
	tts.save('voice.mp3') 
	playsound.playsound('voice.mp3')
	os.remove('voice.mp3')

import speech_recognition as sr
from tts import speak

r = sr.Recognizer()

with sr.Microphone() as source: # 마이크에 담긴 소리를 토대로 아래 코드 실행
    print('인식 중...')
    audio = r.listen(source, timeout=5, phrase_time_limit=5) # 해당 소리를 오디오 파일 형태로 변환
    try:
        result = r.recognize_google(audio, language = "ko-KR") # 오디오를 토대로 음성 인식
        if "고비스" in result or "오피스" in result or "모비스" in result:
            speak("네")   
        elif result == '안녕': # 안녕이라고 말했으면
            speak('안녕하세요') # 컴퓨터가 안녕하세요라고 응답
        elif result == '검색':
            speak('네이버에 검색합니다.')
        elif result == '날씨':
            speak('오늘의 날씨는')
        elif result == '미세먼지':
            speak('오늘의 미세먼지는 ')
        else:
            speak("다시 말씀해주세요.")
    except sr.UnknownValueError:
        speak("이해하지 못하는 말이에요")
    except sr.RequestError:
        speak("서버 에러 발생")
    except sr.WaitTimeoutError:
        speak("인식 실패")

    