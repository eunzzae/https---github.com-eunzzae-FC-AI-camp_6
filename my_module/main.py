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
        print("인식 중...")
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        
    try:
        print("인식 중...")
        query = r.recognize_google(audio, language = "ko-KR")
        print(f'{query}\n')
        return query
    except Exception as e:
        print("다시 말씀해주세요.")
    
if __name__ == "__main__":
    # wishMe()
    call_JiNi()

    while True:
        try:
            print("인식 중...")
            query = takeCommand()
            print(f'{query}\n')
            if query == '검색' or '검색해줘' or '네이버':
                speak("뭘?")
                query = takeCommand()
                keyword = query
                search_naver(keyword)
                
                print("인식 중...")
                query = takeCommand()
                # print(f'{query}\n')  
                if query == '날씨' or "날씨 상태":
                    speak("지역은?")
                    query = takeCommand()
                    location = query
                    speak(f"{location}의 날씨는 다음과 같습니다.")
                    weather_sta(location)
                    # continue
                    print("인식 중...")
                    query = takeCommand()
                    # print(f'{query}\n')
                    
                elif query == '기온' or "기온 검색":
                    speak("지역은?")
                    query = takeCommand()
                    location = query
                    weather_temp
                
                    print("인식 중...")
                    query = takeCommand()
                    # print(f'{query}\n')
                elif query == '미세먼지' or "미세먼지 상태":
                    speak("지역은?")
                    query = takeCommand()
                    location = query
                    weather_air
            # elif '시간' in query or "지금 몇 시야?":
            #     strTime = datetime.datetime.now().strftime("%H:%M:%S")
            #     speak(f'은채님, 지금 시간은 {strTime}')
            
            # elif '잘 가' in query:
            #     speak("좋은 하루 보내요.")
            # exit()    
        except sr.UnknownValueError:
            print("음성 인식 실패")
        except sr.RequestError:
            print("서버 에러 발생")
        except sr.WaitTimeoutError:
            print("인식 실패")

# if __name__=="__main__":
#     # wishMe()
#     voice_call()


# def voice_call():
#     while True:
#         try:
#             with mic as source: # 마이크에 담긴 소리를 토대로 아래 코드 실행
#                 print('인식 중...')
#                 audio = r.listen(source, timeout=7, phrase_time_limit=5)
#                 result = r.recognize_google(audio, language = "ko-KR")
#                 print(result)
#                 if "시리" in result or "시리야" in result or "이리" in result:
#                     speak("네")
#                     print('인식 중...')
#                     print(result)
#                     while True:
#                         if "검색" in result or "검색해줘" in result or "검색" in result:
#                             naver() 
#                             print(result)
#                             speak()

#         except sr.UnknownValueError:
#             speak("다시 말씀해주세요.")