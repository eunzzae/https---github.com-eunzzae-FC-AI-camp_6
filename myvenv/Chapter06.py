from bs4 import BeautifulSoup

# HTML 문서를 문자열 html로 저장
html = '''
<html> 
    <head> 
    </head> 
    <body> 
        <h1> 장바구니
            <p id='clothes' class='name' title='라운드티'> 라운드티
                <span class = 'number'> 25 </span> 
                <span class = 'price'> 29000 </span> 
                <span class = 'menu'> 의류</span> 
                <a href = 'http://www.naver.com'> 바로가기 </a> 
            </p> 
            <p id='watch' class='name' title='시계'> 시계
                <span class = 'number'> 28 </span>
                <span class = 'price'> 32000 </span> 
                <span class = 'menu'> 액세서리 </span> 
                <a href = 'http://www.facebook.com'> 바로가기 </a> 
            </p> 
        </h1> 
    </body> 
</html>
'''
# 바로 아래에 있는 태그는 자식/더 안에 있는 태그는 자손

# 1. 문자열 -> html 구조로 변환
soup = BeautifulSoup(html, 'html.parser') #BeautifulSoup(문자열 html, 파사)
# result = soup.select('body > h1') #자손인 태그 말고 자식인 h1 태그만 가져오게 됨
#print(result) # 리턴값은 무조건 리스트임

# 2. 태그이름/클래스이름을 특정해서 우리가 원하는 정보(태그)를 추출
result=soup.select('#watch .price')

#3. 텍스트 부분만 추출
print(result[0].text.strip())

# - soup.select('태그명') : 태그를 입력으로 사용할 경우
# - soup.select('.클래스명') : 클래스를 입력으로 사용할 경우 (`.` 은 클래스를 뜻하는 특수기호입니다.)
# - soup.select('#아이디') : ID를 입력으로 사용할 경우 (`#` 은 id를 뜻하는 특수기호입니다.)
# - soup.select('상위태그명 하위태그명') : 자손 관계 (어떤 태그 내부에 있는 모든 태그를 자손이라고 함)
# - soup.select('상위태그명 > 하위태그명') : 자식 관계 (어떤 태그 내부에 있는 태그 중 바로 한 단계 아래에 있는 태그를 자식이라고 함)

# 1.태그명
# result = soup.select('span')
# print(result)

# 2.클래스명
# result = soup.select('.price')
# print(result)

# 3.ID
# result = soup.select('#watch')
# print(result)