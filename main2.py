import speech_recognition as sr
from playsound import playsound
import os
from tts import speak
from stt import listen
from naver import *
from weather import *

if __name__ == "__main__":
    text = listen()
    speak(text)
    
while True:
    try:
        query = listen()
        print(f'{query}\n')
        if '검색' in query:
            speak("뭘?")
            query = listen()
            keyword = query
            search_naver(keyword)
            
            query = listen()
            # print(f'{query}\n')  
        elif '날씨' in query:
            speak("지역은?")
            query = listen()
            location = query
            weather_sta(location)
            # continue
            
            query = listen()
            # print(f'{query}\n')
        elif '기온' in query:
            speak("지역은?")
            query = listen()
            location = query
            weather_temp(location)
        
            query = listen()
            # print(f'{query}\n')
        elif '미세먼지' in query:
            speak("지역은?")
            query = listen()
            location = query
            weather_air(location)

    except sr.UnknownValueError:
        print("음성 인식 실패")
    except sr.RequestError:
        print("서버 에러 발생")
    except sr.WaitTimeoutError:
        print("인식 실패")
        
