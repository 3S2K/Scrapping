from Scrapers.ScraperManager import ScraperManager
from Info import youtube_urls
from Info import news_url

if __name__ == "__main__":
    driver_path = "C:\\Users\\home\\Documents\\edgedriver_win64\\msedgedriver.exe"
    channel_name = "썰송이"
    scraper_manager = ScraperManager(driver_path)
    scraper_manager.start_scraping_processes(channel_name, youtube_urls, news_url)
