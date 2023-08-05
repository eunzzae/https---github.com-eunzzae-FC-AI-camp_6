import requests
from bs4 import BeautifulSoup
import csv

def crawl_naver(category, date, page):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    url = f'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1={category}&date={date}&page={page}'
    response = requests.get(headers=headers, url=url)

    soup = BeautifulSoup(response.text, 'html.parser')

    news_list = soup.select('.type06_headline li dl')
    
    result_list=[['제목', '본문일부', '신문사', '작성시각']]
    for news in news_list:
        try:
            title = news.select('a')[1].text.strip()
        except IndexError:
            title = news.select('a')[0].text.strip()
        content = news.select('.lede')[0].text
        writing = news.select('.writing')[0].text
        datetime = news.select('.date')[0].text
        result_list.append([title, writing])
        
    with open('news_list.csv','a', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerows(result_list)
        
crawl_naver(103, 20230101, 1)