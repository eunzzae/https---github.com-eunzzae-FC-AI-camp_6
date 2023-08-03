#멜론 크롤링 실습

import requests
import csv
from bs4 import BeautifulSoup


headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
url = 'https://www.melon.com/chart/index.htm'
response = requests.get(headers=headers, url=url)
        
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select('.lst50 .rank01 a')
artists = soup.select('.lst50 .rank02 > a')
music_list = [['제목', '가수']]
    
for i in range(50):
    music_list.append([titles[i].text, artists[i].text])
with open('melon_chart.csv', 'a', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerows(music_list)