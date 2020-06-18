# 다음에서 뉴스 1건의 기사와 내용을 수집

import requests
from bs4 import BeautifulSoup

url = 'https://news.v.daum.net/v/20200616082721019'
resp = requests.get(url)

if resp.status_code == 200:
    print('success')
else:
    print('Wrong URL')

soup = BeautifulSoup(resp.text,'html.parser')
title = soup.select('h3.tit_view')    #title 은 복수의 데이터를 가져올것을 예상해 결과값을 List로 받아온다.
contents = soup.select('div#harmonyContainer p')

text = ''
for i in contents:
    text += i.text

print(text)


print(title[0].text)    #번지수값을 지정해서 출력하면 된다.
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print(contents[0].text)   # strip() 은 문단과 문단 사이 사이 공백 제거 안됨 다른곳 공백제거 해주는것


title = soup.select('div.article_view')
print(title[0].text)