# import pyttsx3
# import datetime
# import speechRecognition as sr
# import webbrowser
# import naver
# import weather_func

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices') # 목소리를 세세하게 전달
# engine.setProperty('voice', voices[1].id)

# # 말하는 함수 
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
# user = '은채'

# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("은채님, 좋은 아침입니다.")
#     elif hour>=12 and hour < 18:
#         speak("은채님, 좋은 오후입니다.")
#     else:
#         speak("은채님, 좋은 저녁입니다. ")

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("인식 중...")
#         r.pause_threshold = 1
#         audio = r.listen(source, timeout=7, phrase_time_limit=5)
        
#     try:
#         print("입력 중...")
#         query = r.recognize_google(audio, language = "ko-KR")
#         print(f'출력 : {query}\n')
    
#     except Exception as e:
#         print("다시 말씀해주세요.")
#         return "None"
#     return query
    
# if __name__ == "__main__":
#     wishMe()
#     while True:
#         query = takeCommand().lower()
#         if '지니' in query in query or '지니야' in query or '지니 안녕':
#             speak('네, 무엇을 도와드릴까요?')
            
#         if 'search_naver' in query:
#             speak("네이버에서 검색중입니다.")
#             query = query.replace("naver", "")
#             results = naver.summary(query, sentences=2)
#             speak("네이버에 따르면")
#             print(results)
#             speak(results)
            
#         elif 'open_google' in query:
#             webbrowser.open("google.com")
            
#         elif 'the time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f'은채님, 지금 시간은 {strTime}')
            
#         elif 'exit' in query:
#                 speak("Thanks for giving me your time ..... have a nice day....")
#         exit()    
# except sr.UnknownValueError:
# print("음성 인식 실패")
# except sr.RequestError:
# print("서버 에러 발생")
# except sr.WaitTimeoutError:
# print("인식 실패")
