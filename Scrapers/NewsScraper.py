from Crawlers.NewsCrawler import NewsCrawler


class NewsScraper:
    def __init__(self, driver_path):
        self.news_crawler = NewsCrawler(driver_path)

    def scrape_news(self, news_url):
        self.news_crawler.open_news_site(news_url)
        print("뉴스 크롤링 작업 수행 완료")
        self.news_crawler.quit()
