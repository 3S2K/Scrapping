from multiprocessing import Process
from Scrapers.YouTubeScraper import YouTubeScraper
from Scrapers.NewsScraper import NewsScraper
from Parsers.YouTubeParser import YouTubeTranscriptExtractor
import json


def execute_youtube_scraper(driver_path: str, youtube_urls: dict, output_file: str):
    youtube_scraper = YouTubeScraper(driver_path)
    youtube_transcript_extractor = YouTubeTranscriptExtractor()
    youtube = youtube_scraper.scrape_shorts(youtube_urls)
    print("수집된 유튜브 데이터:", youtube)




    # JSON 파일로 저장
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(youtube, file, ensure_ascii=False, indent=4)


def execute_news_scraper(driver_path, news_url, output_file):
    news_scraper = NewsScraper(driver_path)
    news = news_scraper.scrape_news(news_url)
    print("수집된 뉴스 데이터:", news)
    # JSON 파일로 저장
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(news, file, ensure_ascii=False, indent=4)


class ScraperManager:
    def __init__(self, driver_path):
        self.driver_path = driver_path

    def start_scraping_processes(self, youtube_urls, news_url):
        youtube_output_file = "data/youtube_data.json"
        news_output_file = "data/news_data.json"

        youtube_process = Process(target=execute_youtube_scraper, args=(self.driver_path, youtube_urls, youtube_output_file))
        news_process = Process(target=execute_news_scraper, args=(self.driver_path, news_url, news_output_file))

        youtube_process.start()
        news_process.start()

        youtube_process.join()
        news_process.join()


