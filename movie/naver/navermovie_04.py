import  requests
from bs4 import  BeautifulSoup

# 한페이지만 출력할려고 하는게 아니라 영화 평점에 존재하는 모든 페이지를 출력하는 방법
# navermovie_02 처럼 하면 멈추는게 아니라 계속 마지막페이지가 끝나지 않고 출력이 된다 
# 그러므로 그것에대한 해결방안
cnt = 0
page = 0
compare_writer = ''
break_point = False # 이중반복문을 빠져나가기 위한 포인트

while True:
    page += 1
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=191436&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(page)
    resp = requests.get(url)

    if resp.status_code != 200:
        print('존재하지 않는 URL')
    else:
        soup = BeautifulSoup(resp.text, 'html.parser')
        reply_list = soup.select('div.score_result li')

        for i, reply in enumerate(reply_list):
            cnt += 1
            content = reply.select('div.score_reple p span')[0].text.strip()         # 영화 댓글 내용
            previous_write = reply.select('div.score_reple a  span')[0].text.strip() # 영화 댓글 작성자
            cut_index = previous_write.find('(')                                     # 작성자에 닉네임만 추출하기위한 index번호 계산
            reg_date = reply.select('div.score_reple  em')[1].text.strip()[:10]      # 영화 댓글 작성일자
            score = reply.select('div.star_score  em')[0].text.strip()               # 영화댓글 평점

            # 네이버 영화 댓글의 작성자는 닉네임(아이디) 구조
            # ex) 초롱이(ccw***) -> 닉네임만 추출(그러나 닉네임이 없는 경우도 있음)
            # 닉네임이 없는 경우 ()안의 아이디를 사용하는 코드 작성
            writer = ''
            if cut_index > 0:
                writer = previous_write[:cut_index]
            else:
                writer = previous_write

              # 네이버 영화 댓글 수집 페이지의 마지막 페이지를 계산하는 코드
              #네이버는 1명의 작성자가 1개의 댓글만 작성할 수 있음
              # 매페이지의 첫반째 게시글의 작성자를 compare_writer에 저장하고
              # 매페이지의 첫번째 게시글 작성자와 compare_writer를 비교해서 같으면 중복페이지 -> 수집종료
              # 지금 작성자 수집
            if i == 0:
                if compare_writer != writer:
                    compare_writer = writer
                else:
                    print('Finished Collect:)')
                    break_point = True

            print('■■■■■■■■■■■■■■■■■■■■■■')
            print('내용:', content)
            print('작성자:', previous_write)
            print('평점:', score)
            print('작성일자:', reg_date)
            print('■■■■■■■■■■■■■■■■■■■■■■')

        # 이중반복문 breake
        if break_point:
            break
print('수집한 영화 댓글은 총{}건 입니다'.format(cnt))
            