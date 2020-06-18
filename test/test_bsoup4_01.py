# beautifulsoup4 import
import requests
from bs4 import BeautifulSoup
url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=421&aid=0004696358'
# url 사이트에서 get방식으로 requests를 하면
# return으로 사이트의 html code를 전달
resp = requests.get(url) # 해당페이지를가서 모든 코드 소스를 가져오는것

if resp.status_code == 200:  #상태코드 url에 request 보내고 response 받을때 200번대가 들어오면 정상
                             # 400 번대 500번대가 들어오면 잘못된것 이므로 표시를 해라 라는 코드
    resp.headers
else:
    print('잘못된 URL입니다. 다시 입력해주세요.')

soup = BeautifulSoup(resp.text, 'html.parser')
title = soup.find('h3', id='articleTitle') # h3  중에서 id가 atricleTitle를 찾아라
contents = soup.find('div', id='articleBodyContents')
print(title.text)  # .text 하면 text 만 가져올수있다.
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print(contents.text.strip())






