from Crawlers.YouTubeCrawler import YouTubeCrawler, YouTubeTranscriptExtractor


class YouTubeScraper:
    def __init__(self, driver_path):
        self.youtube_crawler = YouTubeCrawler(driver_path)
        self.transcript_extractor = YouTubeTranscriptExtractor()
        self.captions_data = {}

    def scrape_shorts(self, youtube_urls):
        for channel_name in youtube_urls:
            if channel_name not in youtube_urls:
                raise ValueError("유효한 채널 이름이 아닙니다.")

            channel_url = youtube_urls[channel_name]
            self.youtube_crawler.open_page(channel_url)
            self.youtube_crawler.scroll_until_end()

            shorts_items = self.youtube_crawler.get_all_shorts_elements()

            for item in shorts_items:
                title, link = self.youtube_crawler.get_title_and_link(item)
                if title and link:
                    self.captions_data[title] = link
            print(len(shorts_items))
        self.youtube_crawler.quit()
        return self.captions_data
