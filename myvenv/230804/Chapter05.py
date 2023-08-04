import requests
import csv
import json

#params 부분이 주소에 들어가는 정보
# 네이버 뉴스 -> data/category
params = {
	'serviceKey': 'maKWbyk8A8+f/7PHbgoC/IKn2ggLR5gzKo2zjSkg6oWOx4QhhAlBfSefK31HyS2RvOL+QZO+gXutp7t9o2c8hA==',
	'returnType': 'json',
	'numOfRows': '100',
	'pageNo': '1',
	'sidoName': '서울', # 어떻게 바꾸냐에 따라 데이터가 달라짐
	'ver': '1.0',
}

response = requests.get('http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty', params=params)
data = json.loads(response.text) # 문자열에 불과함 (파이썬 상의 리스트/딕셔너리)
airinfo_list = data['response']['body']['items'] # 리스트로 변환

result=[['측정소명', '시/도명', '미세먼지 수치']]
for airinfo in airinfo_list:
    result.append([airinfo['stationName'], airinfo['sidoName'], airinfo['pm25Value']])

with open('airinfo.csv','a', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerows(result)    