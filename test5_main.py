import speech_recognition as sr
from playsound import playsound
import os
# from stt import listen
from gtts import gTTS
from naver import *
from weather import *


# def call_JiNi():
#     with sr.Microphone() as source:
#         print("인식 중...")
#         audio = r.listen(source)
#         say = r.recognize_google(audio, language='ko-KR')
#         print('[은채]'+say)
#         if say == '지니' or '지미' :
#             speak('안녕하세요.')
#         else:
#             speak('이름을 다시 말해주세요.')


# audio1 = 'search.mp3'
# audio2 = 'temp.mp3'
# audio3 = 'weather.mp3'
# audio4 = 'air.mp3'
# playsound(audio2)

# 음성 인식
def listen2(recognizer, audio):
    with sr.AudioFile('temp.mp3') as source:
        print("인식 중...")
        audio = r.record(source)    
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[은채]'+text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패')
    except sr.RequestError as e:
        print(f'요청 실패 :{e}')
    return

# 대답
def answer(input_text):
    answer_text = ''
    if '검색' in input_text:
        keyword = input('검색어를 입력해주세요. :')
        search_naver(keyword)

    elif '기온' in input_text:
        location = input('위치 : ')
        answer_text = weather_temp(location)
        
    elif '날씨' in input_text:
        location = input('위치 : ')
        answer_text = weather_sta(location)

    elif '미세먼지' in input_text:
        location = input('위치 : ')
        answer_text = weather_air(location)

    elif '종료' in input_text:
        answer_text = '좋은 하루 되세요.'
        stop_listening(wait_for_stop=False) # 더이상 듣지 않음
    else:
        answer_text = '다시 말씀해주세요.'
    
    speak(answer_text)
    
    return 

# 소리내기(tts)
def speak(text):
    print('[지니]' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    # if os.path.exists(file_name): # voice.mp3 파일 삭제
    #     os.remove(file_name)

r = sr.Recognizer()
mic = sr.Microphone()

# # if __name__ == "__main__":
# #     call_JiNi()
# stop_listening = r.listen_in_background(mic, listen2)

while True:
    time.sleep(0.1)

