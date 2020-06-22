package naver;

import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class NavreBoxOffice {

	public static void main(String[] args) throws IOException {
		String url = "https://movie.naver.com/movie/running/current.nhn";
		String titel = ""; // 제목
		String starScore = "dd > span.link_txt > a"; // 평점
		String type = ""; // 장르
		String bookRate = ""; // 예매율
		String movieTime = ""; // 상영시간
		String openDt = ""; // 개봉일
		String director = ""; // 감독
		String actor = ""; // 출연진
		String naverCode = ""; // 네이버 영화 코드

		Document doc = Jsoup.connect(url).get();

		Elements movieList = doc.select("div.lst_wrap > ul.lst_detail_t1 > li");

		for (Element movie : movieList) {
			bookRate = "0";
			director = "";
			actor = "";
			titel = movie.select("dt.tit > a ").text();

			if (movie.select("span.num").size() == 2) {
				bookRate = movie.select("span.num").get(1).text();
			}

			starScore = movie.select("span.num").get(0).text();
			type = movie.select("dd > span.link_txt").get(0).text();
			actor = movie.select("dd > span.link_txt").get(1).text();
			director = movie.select("dd > span.link_txt").get(1).text();

			
			
			String temp = movie.select("dl.info_txt1 > dd").get(0).text();
			int beginTimeIndex = temp.indexOf("|");
			int endTimeIndex = temp.lastIndexOf("|");

			if (beginTimeIndex == endTimeIndex) { // 상영시간
				movieTime = temp.substring(0, endTimeIndex);
			} else {
				movieTime = temp.substring(beginTimeIndex + 2, endTimeIndex);
			}

			int dCode = 0;
			int aCode = 0;
			if (!movie.select("dit.tit_t2").text().equals("")) {
				dCode = 1; // 감독있음!
			}
			if (!movie.select("dit.tit_t3").text().equals("")) {
				aCode = 1; // 출연진있음!
			}

			if (dCode == 1 && aCode == 0) {
				director = movie.select("dd > span.link_txt").get(1).text();// 감독
			} else if (dCode == 0 && aCode == 1) {
				actor = movie.select("dd > span.link_txt").get(1).text();// 출연진
			} else if (dCode == 1 && aCode == 1) {
				director = movie.select("dd > span.link_txt").get(1).text();
				actor = movie.select("dd > span.link_txt").get(2).text();// 출연진
			}

			String naverHref = movie.select("dt.tit > a ").attr("href");// 네이버 영화 코드
			naverCode = naverHref.substring(naverHref.lastIndexOf("=") + 1);
			// 영화 개봉일자.
			int openDtTxtIndex = temp.lastIndexOf("개봉");
			openDt = temp.substring(endTimeIndex + 2, openDtTxtIndex);
			System.out.println("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■");
			System.out.println(String.format("■영화제목 : " + titel));
			System.out.println(String.format("■영화평점: " + starScore + "점"));
			System.out.println(String.format("■예매율: " + bookRate, "%"));
			System.out.println(String.format("■장르: " + type));
			System.out.println(String.format("■상영시간: " + movieTime));
			System.out.println(String.format("■감독: " + director));
			System.out.println(String.format("■개봉일: " + openDt));
			System.out.println(String.format("■무비코드: " + naverCode));

			System.out.println("사이즈>>>>>>>>>>>>>>" + movie.select("dd > span.link_txt"));

		}

	}
}
