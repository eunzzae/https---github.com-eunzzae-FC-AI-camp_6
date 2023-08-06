#실습
import requests
import csv
from bs4 import BeautifulSoup

def crawl_naver(category, data, page):
    # 1. get 요청 보내고 (headers를 포함해서 보안을 우회 - 내가 브라우저로 접근하는게 맞다고 해줌)
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    response = requests.get(f'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=103', headers=headers)
    #필수적***** -> 응답 제대로 왔는지 확인 필요(브라우저상 html과 파이썬상 응답이 동일할거란 보장없음)

    # 2. 응답(문자열) -> html 구조로 변환
    soup = BeautifulSoup(response.text, 'html.parser')

    # 3. 변환한 그 데이터에서 .select 써서 원하는 태그 추출
    tags = soup.select('.type06_headline li')

    # 4. 그 태그에서 글자만 추출하는 가공 작업 진행(파이썬의 영억) 
    result=[]
    for tag in tags:
        try:
            title=tags[2].select('a')[1].text.strip() #사진이 있는 기사들은 2번째 a태그
        except IndexError:
            title = (tags[2].select('a')[1].text.strip()) #사진이 없는 기사들은 1번째 a태그
        writing=tag.select('.writing')[0].text # 기사 신문사
        content=tag.select('.lead')[0].text
        date=tag.select('.date')[0].text
        result.append([title, writing, content, date])
    # 5. csv로 저장하는 작업 진행
    with open('news.csv','a', encoding='utf-8-sig') as f:
        writer = csv.writer(f) # 쓰기 위한 객체 생성
        writer.writrows(result) # news.csv에다가 우리가 가진 result 리스트를 행/열 맞춰서 입력

crawl_naver(105, 20230103, 1)

