# 다음 뉴스 한 페이지에서 뉴스 기사와 내용을 수집(15건의 기사)

import requests
from bs4 import BeautifulSoup
# url은 내가 수집하고 싶은 데이터가 위치한 웹 사이트 주소를 가리킴!
url = 'https://news.daum.net/breakingnews/digital'
# url 주소를 이용해서 해당 웹페이지의 모든 소스코드를 불러와서 resp에 저장
resp = requests.get(url)

soup = BeautifulSoup(resp.text,'html.parser')

# resp에 staus_code가 200이면 성공, 나머지는 실패
if resp.status_code == 200:
    print('Success')
    pass
else:
    print('Wrong URL')
    pass

# requests는 소스코드만 전부 가져오는거고 거기서 원하는 내용을 추출 불가!!
# BeautifulSoup에 input으로 resp의 값(웹사이트의 소스코드 전체)을 전달
# soup에 웹사이트의 소스코드 전체가 저장
# soup.select()를 이용하여 원하는 정보만 추출
url_list = soup.select('ul.list_allnews a.link_txt')
for i in url_list:

    url = i['href']
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    title = soup.select("h3.tit_view") #(태그+선택자)
    contents = soup.select('div#harmonyContainer p')
# soup.select()는 무조건 return을 list type으로 반환
#[val1, val2, val3, ....]
# ex) contents[1]
    print(title[0].text)
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

    text = ''
    for j in contents:
        text += i.text + '\n'

    print(text)


