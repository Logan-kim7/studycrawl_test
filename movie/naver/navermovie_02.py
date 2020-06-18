import  requests
from bs4 import  BeautifulSoup

# 한페이지만 출력할려고 하는게 아니라 영화 평점에 존재하는 모든 페이지를 출력하는 방법
cnt = 0
page = 1
while True:

    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=191436&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(page)
    resp = requests.get(url)

    if resp.status_code != 200:
        print('존재하지 않는 URL')
    else:
        soup = BeautifulSoup(resp.text, 'html.parser')
        reply_list = soup.select('div.score_result li')


        for reply in reply_list:
              content = reply.select('div.score_reple p span')[0].text.strip()         # 영화 댓글 내용
              previous_write = reply.select('div.score_reple a  span')[0].text.strip() # 영화 댓글 작성자
              cut_index = previous_write.find('(')                                     # 작성자에 닉네임만 추출하기위한 index번호 계산
              reg_date = reply.select('div.score_reple  em')[1].text.strip()[:10]      # 영화 댓글 작성일자
              score = reply.select('div.star_score  em')[0].text.strip()               # 영화댓글 평점



              # 네이버 영화 댓글의 작성자는 닉네임(아이디) 구조
              # ex) 초롱이(ccw***) -> 닉네임만 추출(그러나 닉네임이 없는 경우도 있음)
              # 닉네임이 없는 경우 ()안의 아이디를 사용하는 코드 작성


              if cut_index > 0:
                  writer = previous_write[:cut_index]
              else:
                  writer = previous_write


              print('■■■■■■■■■■■■■■■■■■■■■■')
              print('내용:', content)
              print('작성자:', previous_write)
              print('평점:', score)
              print('작성일자:', reg_date)
              print('■■■■■■■■■■■■■■■■■■■■■■')

    page += 1
