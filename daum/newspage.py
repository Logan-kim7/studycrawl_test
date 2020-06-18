import requests
from bs4 import BeautifulSoup
cnt = 0
for i in range(1, 4):
    url = 'https://news.daum.net/breakingnews/digital?page={}'.format(i)

    resp =requests.get(url)
    soup = BeautifulSoup(resp.text,'html.parser')


    if resp.status_code == 200:
        print('Success')
        pass
    else:
        print('Wrong URL')
        pass

    url_list = soup.select('ul.list_allnews a.link_txt')
    for j in url_list:


        cnt += 1
        url = j['href']
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        title = soup.select("h3.tit_view")
        contents = soup.select('div#harmonyContainer p')

        text = ''
        for k in contents:
            text += k.text + '\n'
        print('=========================================================')
        print(title[0].text)
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print(text)

print('▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶')
print('{}건의 뉴스기사를 수입하였습니다.'.format(cnt))
print('▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶')
