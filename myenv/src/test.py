import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105'
response = requests.get(url)

# print(response.status_code) # 응답코드

html = response.text # HTML 코드
soup = BeautifulSoup(html, 'html.parser')

it_news_title_ul = soup.select_one('ul.sh_list')
it_news_titles = it_news_title_ul.select('li > .sh_text > a')
titles = []

for title in it_news_titles:    
  titles.append(title.get_text())
  
title_list = {"뉴스타이틀" : titles}  
# print(title_list)  

# 가정: data는 딕셔너리 형태의 크롤링 데이터
df = pd.DataFrame(title_list)
df.to_excel("C:\work\python_projects\data.xlsx", index=False)