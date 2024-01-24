from requests import get
from bs4 import BeautifulSoup

def extract_naver_news(keyword):
    url = f"https://search.naver.com/search.naver?where=news&query={keyword}&sm=tab_opt&sort=1&photo=0&field=0&pd=4&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:dd,p:1d&is_sug_officeid=0&office_category=0&service_area=0"
    response = get(url)
    if response.status_code != 200:
        print("Can't request naver news")
    else:
        results = []
        print("Success to request naver news")
        soup = BeautifulSoup(response.text, "html.parser")
        newses = soup.find_all("div", class_="news_area")
        for news in newses:
            title_block = news.find("a", class_="news_tit")
            title = title_block['title']
            link = title_block['href']
            press = news.find("a", class_="press").text
            time = news.find("span", class_="info").text
            
            news_data = {
                "title": title,
                "press": press,
                "time": time,
                "link": link
            }
            results.append(news_data)
        return results