

import requests
from bs4 import BeautifulSoup

# 페이지를 돌면서, 내용, 작성일자, 작성자 수집하는 코드
cnt = 0
for page in range(1, 6):
    list_url = 'http://news.sarangbang.com/bbs.html?tab=story&p={}'.format(page)  # 여기만 수정하면됨
    resp = requests.get(list_url)

    if resp.status_code != 200:
        print('WARNING: 잘못된 URL 접근!!')

    soup = BeautifulSoup(resp.text, 'html.parser')
    board_list = soup.select('tbody#bbsResult a#gLsbj_578015')     # tr > td > a :not(.name_more)
    # print(board_list)

    for i, href in enumerate(board_list):
        # print(i,href)

        cnt += 1
        print('http://news.sarangbang.com'+href['href'])




        url = 'http://news.sarangbang.com' + href['href']
        resp = requests.get(url)

        if resp.status_code != 200:
            print('WARNING: 잘못된 URL 접근')

        soup = BeautifulSoup(resp.text, 'html.parser')
        title = soup.select('h3.tit_view')[0].text.strip()
        write = soup.select('a.name_more')[0].text.strip()
        content = soup.select('div.bbs_view p') + soup.select('div.bbs_view div')
        reg_dt = soup.select('span.tit_cat')[1].text.strip()[:10]


        print('TITTLE ▶▶▶▶▶', title)
        print('NAME ▶▶▶▶▶', write)
        print('REG_DT ▶▶▶▶▶', reg_dt)
        print(reg_dt)

        contents = ""
        for i in content:
            contents += i.text.strip()
        print('CONTENTS ▶▶▶▶▶', contents)
print('사랑방 부동산에서 {}건의 게시글을 수집하였습니다.'.format(cnt))