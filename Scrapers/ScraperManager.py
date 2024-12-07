from multiprocessing import Process
from Scrapers.YouTubeScraper import YouTubeScraper
from Scrapers.NewsScraper import NewsScraper
import json


def execute_youtube_scraper(driver_path: str, youtube_urls: dict, output_file: str):
    youtube_scraper = YouTubeScraper(driver_path)
    youtube = youtube_scraper.scrape_shorts(youtube_urls)
    # JSON 파일로 저장
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(youtube, file, ensure_ascii=False, indent=4)


def execute_news_scraper(driver_path: str, news_url: str, output_file: str):
    news_scraper = NewsScraper(driver_path)
    news = news_scraper.scrape_news(news_url)
    # JSON 파일로 저장
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(news, file, ensure_ascii=False, indent=4)


class ScraperManager:
    def __init__(self, driver_path: str):
        self.driver_path = driver_path

    def start_scraping_processes(self, youtube_urls: dict, news_url: str):
        youtube_output_file = "data/youtube_data.json"
        news_output_file = "data/news_data.json"

        youtube_process = Process(target=execute_youtube_scraper, args=(self.driver_path, youtube_urls, youtube_output_file))
        news_process = Process(target=execute_news_scraper, args=(self.driver_path, news_url, news_output_file))

        youtube_process.start()
        news_process.start()

        youtube_process.join()
        news_process.join()


