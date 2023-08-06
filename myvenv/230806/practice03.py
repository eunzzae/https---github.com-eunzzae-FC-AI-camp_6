# 웹 크롤링 
# 멜론 차트 100위까지 순위가져오기

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

def openDriver():
    url = 'https://www.melon.com/chart/index.htm'
    driver = webdriver.Chrome()
    # time_sleep() 과 비슷하지만 웹크롤링 할 때는 이 함수를 사용하는 것이 좋음
    driver.implicitly_wait(3) 
    driver.get(url)
    time.sleep(1)
    return driver

def searchMelon(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all(class_='wrap_song_info')
    
    melon_list=[]
    rank=1
    for i in tags:
        try:
            titles = i.find(class_='ellipsis rank01').a.text 
            artists = i.find(class_='ellipsis rank02').a.text 
            print(f'순위 : {rank}\n 가수 : {artists}\n 제목 : {titles}\n')
            melon_list.append([rank, artists, titles])
            rank += 1
        except:
            pass
    return melon_list

def saveToFile(filename, melon_list):
    with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(melon_list)
        
driver = openDriver()
melon_list=searchMelon(driver)
saveToFile('melon.csv', melon_list)