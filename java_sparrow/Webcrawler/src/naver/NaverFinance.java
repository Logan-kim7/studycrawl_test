package naver;

import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class NaverFinance {
	static String base = "https://finance.naver.com/item/frgn.nhn?code=005930&page=1";

	public static void main(String ars[]) throws IOException {
		// base 사이트로 가서 전체 페이지의 소스코드를 가져옴
		Document doc = Jsoup.connect(base).get();

		// Elements > list와 비슷한 형태로 복수 의 값을 저장할수 있다.
		Elements line = doc.select("table.type2 > tbody > tr");
		// System.out.println(line.size());
		int count = 0;
		// 향상된 for문
		for (Element element : line) {
			Elements tds = element.select("td");
			if (tds.size() == 9) {
				System.out.println("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■");
				String regdate = tds.get(0).text();
				String regamount = tds.get(1).text();
				String regnum = tds.get(2).text();
				String regupdown = tds.get(3).text();
				String regcount = tds.get(4).text();
				String reggosell = tds.get(5).text();
				String reggobuy = tds.get(6).text();
				String reghv = tds.get(7).text();
				String regfohv = tds.get(8).text();

				System.out.println(String.format(
						"날짜 \t: %s\n" + "종가\t: %s\n" + "전일비\t: %s\n" + "등락률\t: %s\n" + "거래량\t: %s\n" + "기관 순매매량\t: %s\n"
								+ "외국인 순매매량\t: %s\n" + "외국인 보유주수\t: %s\n" + "외국인 보유율\t: %s\n",
						regdate, regamount, regnum, regupdown, regcount, reggosell, reggobuy, reghv, regfohv));
				System.out.println("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■");

			}
		}

		/*
		 * jsoup 필요!
		 * 
		 * 
		 * python -> beautifulsoup4 , selenium필요 <- Anaconda(패키지 매니저)
		 */

	}

}
