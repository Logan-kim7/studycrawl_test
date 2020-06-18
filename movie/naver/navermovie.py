import  requests
from bs4 import  BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=191436&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false'
resp = requests.get(url)

if resp.status_code != 200:
    print('존재하지 않는 URL')
else:
    soup = BeautifulSoup(resp.text, 'html.parser')
    reply_list = soup.select('div.score_result li')


    for i, reply in enumerate (reply_list):
          content = reply.select('sapn#_filtered_ment_{}'.format(i))   # str() -> String Type 로 변환
          score = reply.select('div.star_score  em')[0].text.strip()
          reg_date = reply.select('div.score_reple  em')[1].text.strip()[:10]
          previous_write = reply.select('div.score_reple a  span')[0].text.strip()
          cut_index = previous_write.index('(')
      # 네이버 영화 댓글의 작성자는 닉네임(아이디) 구조
      # ex) 초롱이(ccw***) -> 닉네임만 추출(그러나 닉네임이 없는 경우도 있음)
      # 닉네임이 없는 경우 ()안의 아이디를 사용하는 코드 작성
          if cut_index > 0:
              writer = previous_write[:cut_index]
          else:
              writer = previous_write


          print('■■■■■■■■■■■■■■■■■■■■■■')
          print('평점:', score)
          print('작성자:', previous_write)
          print('내용:', content)
          print('작성일자:', reg_date)
          print('■■■■■■■■■■■■■■■■■■■■■■')

