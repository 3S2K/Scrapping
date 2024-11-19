import time


class Scraper:
    def __init__(self, youtube_crawler, news_crawler, transcript_extractor):
        self.youtube_crawler = youtube_crawler
        self.news_crawler = news_crawler
        self.transcript_extractor = transcript_extractor

    def scrape_shorts(self, channel_name, youtube_urls, num_shorts=3):
        if channel_name not in youtube_urls:
            raise ValueError("유효한 채널 이름이 아닙니다.")

        channel_url = youtube_urls[channel_name]
        self.youtube_crawler.open_shorts_channel(channel_url)
        self.youtube_crawler.click_first_shorts()

        captions_data = {}

        for i in range(num_shorts):
            current_url = self.youtube_crawler.get_current_url()
            captions = self.transcript_extractor.fetch_youtube_captions(current_url)
            current_title = self.youtube_crawler.get_current_title()
            captions_data[current_title] = captions
            time.sleep(5)
            print(f"현재 URL: {current_url}")
            print(f"현재 제목: {current_title}")
            self.youtube_crawler.click_next_shorts()

        self.youtube_crawler.quit()
        return captions_data

    def scape_news(self, news_url, num_news=8):
        pass



