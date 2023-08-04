import requests
from bs4 import BeautifulSoup

# 지난 시간 크롤링
# 1. requests 모듈을 써서 웹 주소에 요청을 보내고, 응답으로 HTML을 받아옴
response = requests.get('')

# 2. 그 HTML을 beaurifulsoup 모듈을 써서 파싱(문자열 -> HTML구조)
# 3. 파싱된 데이터를 토대로 우리가 원하는 정보가 있는 태그를 명시해서 추출
