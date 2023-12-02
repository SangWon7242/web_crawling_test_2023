# 웹 크롤링 방법

# 첫 번째 작업
## 파이썬 가상화 환경
```cmd
# 가상환경 설치
python -m venv "폴더명"

# 가상 환경 활성화
myenv\Scripts\activate
```

```python
# 중요 라이브러리 설치
import requests
# 파이썬 HTTP 라이브러리(HTTP, HTTPS 웹 사이트 요청)
# 크롤링 과정에서 requests 모듈 이용해서 소스코드 파싱

from bs4 import BeautifulSoup
# HTML 정보로 부터 원하는 데이터를 쉽게 가져오는 라이브러리

import pandas as pd
# 데이터를 엑셀로 변환시켜주는 라이브러리
```

```python
# url 변수에 내가 크롤링 하고자 하는 대상 url 입력
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105'
response = requests.get(url) # 지정 URL에 get 요청을 보냄
```

```python
html = response.text # HTML 코드
soup = BeautifulSoup(html, 'html.parser')

# 가져오고 싶은 대상 html을 찾음
it_news_title_ul = soup.select_one('ul.sh_list')
# 현재 찾고자 하는 데이터는, 특정 뉴스 기사의 제목
# 뉴스 기사의 제목 html 구조는 ul.sh_list > li > .sh_text > a
# a안에 들어있는 text를 뽑아오는 작업을 통해 뉴스 제목을 가져올 수 있다.
it_news_titles = it_news_title_ul.select('li > .sh_text > a')
```

```python
titles = []

# a엘리먼트로 접근한 데이터에서 get_text() 함수를 이용하여 text만 추출
# 반복문을 이용하여 추출한 기사 제목을 list에 저장
for title in it_news_titles:    
  titles.append(title.get_text())
  
# 엑셀에 저장하기 위해 key : value로 기사 제목을 딕셔너리 형태로 저장  
title_list = {"뉴스타이틀" : titles} 
# print(title_list)  
```

```python
# 가정: data는 딕셔너리 형태의 크롤링 데이터
df = pd.DataFrame(title_list) # 기사 제목을 엑셀 형태로 변환
df.to_excel("C:\work\python_projects\data.xlsx", index=False) # 특정 경로로 엑셀 저장
```