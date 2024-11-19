from Scraper import Scraper
from Crawlers.YouTubeCrawler import YouTubeCrawler, YouTubeTranscriptExtractor
from Crawlers.NewsCrawler import NewsCrawler
from Info import youtube_urls

if __name__ == "__main__":

    driver_path = "C:\\Users\\home\\Documents\\edgedriver_win64\\msedgedriver.exe"
    youtube_crawler = YouTubeCrawler(driver_path)
    news_crawler = NewsCrawler(driver_path)
    transcript_extractor = YouTubeTranscriptExtractor()
    scraper = Scraper(youtube_crawler, news_crawler, transcript_extractor)
    channel_name = "썰송이"
    captions = scraper.scrape_shorts(channel_name, youtube_urls)
    print("수집된 자막 데이터:", captions)
