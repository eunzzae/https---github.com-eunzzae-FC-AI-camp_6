# 기상청 단기예보 조회를 통한 날씨정보

import requests
from datetime import datetime
import xmltodict

def get_current_date_string():
    current_date = datetime.now().date()
    return current_date.strftime("%Y년 %m월 %d일")

def get_current_hour_strint():
    now = datetime.now()
    if now.minute < 45: # base_time과 base_date 구하는 함수
        if now.hour == 0 :
            base_time = '2330'
        else:
            pre_hour = now.hour-1
            if pre_hour < 10:
                base_time = "0" + str(pre_hour) + "30"
            else:
                base_time = str(pre_hour) + "30"
    else:
        if now.hour <10:
            base_time = "0" + str(now.hour) +"30"
        else:
            base_time = str(now.hour) +"30"
    return base_time

