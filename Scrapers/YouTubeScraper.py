from Crawlers.YouTubeCrawler import YouTubeCrawler, YouTubeTranscriptExtractor


class YouTubeScraper:
    def __init__(self, driver_path):
        self.youtube_crawler = YouTubeCrawler(driver_path)
        self.transcript_extractor = YouTubeTranscriptExtractor()

    def scrape_shorts(self, channel_name, youtube_urls, num_shorts=3):
        if channel_name not in youtube_urls:
            raise ValueError("유효한 채널 이름이 아닙니다.")

        channel_url = youtube_urls[channel_name]
        self.youtube_crawler.open_page(channel_url)
        self.youtube_crawler.click_first_shorts()

        captions_data = {}

        for i in range(num_shorts):
            current_url = self.youtube_crawler.get_current_url()
            captions = self.transcript_extractor.fetch_youtube_captions(current_url)
            current_title = self.youtube_crawler.get_current_title()
            captions_data[current_title] = captions
            print(f"현재 URL: {current_url}")
            print(f"현재 제목: {current_title}")
            self.youtube_crawler.click_next_shorts()

        self.youtube_crawler.quit()
        return captions_data
