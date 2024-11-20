

from multiprocessing import Process
from Scrapers.YouTubeScraper import YouTubeScraper
from Scrapers.NewsScraper import NewsScraper


def execute_youtube_scraper(driver_path, channel_name, youtube_urls):
    youtube_scraper = YouTubeScraper(driver_path)
    captions = youtube_scraper.scrape_shorts(channel_name, youtube_urls)
    print("YouTube 수집된 자막 데이터:", captions)


def execute_news_scraper(driver_path, news_url):
    news_scraper = NewsScraper(driver_path)
    news_scraper.scrape_news(news_url)
    pass


class ScraperManager:
    def __init__(self, driver_path):
        self.driver_path = driver_path

    def start_scraping_processes(self, channel_name, youtube_urls, news_url):
        youtube_process = Process(target=execute_youtube_scraper, args=(self.driver_path, channel_name, youtube_urls))
        news_process = Process(target=execute_news_scraper, args=(self.driver_path, news_url))

        youtube_process.start()
        news_process.start()

        youtube_process.join()
        news_process.join()


