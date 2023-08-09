import speech_recognition as sr
from stt import listen
from tts import speak
from lotto_num import *
from naver import *
from weather import *
import datetime

# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("은채님, 좋은 아침입니다.")
#     elif hour>=12 and hour < 18:
#         speak("은채님, 좋은 오후입니다.")
#     else:
#         speak("은채님, 좋은 저녁입니다. ")

def call_JiNi():
    print("인식 중...")
    query = takeCommand()
    print(f'{query}\n')
    if query == '지니' or '지니야' or '지니 안녕':
        speak('네')
    else:
        speak('다시 말씀해주세요.')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("듣는 중...")
        audio = r.listen(source, timeout=10, phrase_time_limit=5)
    try:
        print("인식 중...")
        query = r.recognize_google(audio, language = "ko-KR")
        print(f'{query}\n')
        
    except Exception as e:
        print("다시 말씀해주세요.")
        return ""
    return query

if __name__ == "__main__":
    # wishMe()
    call_JiNi()
    while True:
        query = takeCommand()
        if '검색' or '검색해줘' or '네이버' in query:
            speak("뭘?")
            query = takeCommand()
            keyword = query
            search_naver(keyword) 
            
        elif '날씨' or "날씨 상태" in query:
            speak("지역은?")
            query = takeCommand()
            location = query
            # speak(f"{location}의 날씨는 다음과 같습니다.")
            result = weather_sta(location)
            speak(result)

        elif '기온' or "기온 검색" in query:
            speak("지역은?")
            query = takeCommand()
            location = query
            result = weather_temp(location)
            speak(result)
        
        elif '미세먼지' or "미세먼지 상태" in query:
            speak("지역은?")
            query = takeCommand()
            location = query
            result = weather_air(location)
            speak(result)
                
# except sr.UnknownValueError:
#     print("음성 인식 실패")
# except sr.RequestError:
#     print("서버 에러 발생")
# except sr.WaitTimeoutError:
#     print("인식 실패")

