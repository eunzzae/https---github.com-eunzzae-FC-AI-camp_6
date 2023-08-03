#웹크롤링

# 웹 사이트에 들ㄹ간다.
# # 네이버라는 주소를 입력하면 (네트워크 '요청'이라고 함)
# 그 주소를 운영하고 있는 웹서버가 건네주는 html 파일('응답')을 다운로드 받고
# 그 파일을 웹브라우저가 해석해서 보여주는것

# 웹 사이트 요청
# GET 요청 -> 좀 줘 (네이버에 들어가는건 네이버 html 파일 좀 줘 -> GET요청)
# 식당에서 메뉴판달라고 하는거 -> 돈이 필요한가? 필요없음 
# (보안장치가 없는 한) 아무것도 없이 요청해도 됨

# POST 요청 -> 좀 등록해줘(네이버에서 블로그 같은 곳에서 글을 쓰는 것 -> POST요청)
# 글을 쓴다 -> 정확히 어떤 글? 우리가 글을 써서 전달해줘야 함
# 요청보낼 때 데이터가 필요함(e.g. 글)
# 글을 쓰면 영구적으로 네이버 서버에 등록이 됨

# requests 설치

import requests
import json
# requests.get('주소')
# requests.post('주소', 보낼 데이터)


#response=requests.get('https://www.naver.com/')
#print(response.text[0:10])

#beautifulsoup
response=requests.get('https://www.naver.com/')
print(response.text) #문자열 -> html구조로 변환(beautifulsoup, 파싱)
# A태그 가져와
# class가 ~인 태그 가져와

# <태그이름 속성 ="값">내용</태그이름>
# <h1 속성 ="값">내용</h1>
# response=requests.post('https://jsonplaceholder.typicode.com/posts', {'title':'내 글','body' : '내용'})
# print(response.text)
