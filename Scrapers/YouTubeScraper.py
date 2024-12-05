from Crawlers.YouTubeCrawler import YouTubeCrawler
from Parsers.YouTubeParser import YouTubeTranscriptExtractor, is_scraped
import json


class YouTubeScraper:
    def __init__(self, driver_path):
        self.youtube_crawler = YouTubeCrawler(driver_path)
        self.youtube_parser = YouTubeTranscriptExtractor()
        self.captions_data = {}

    def scrape_shorts(self, youtube_urls):
        try:
            with open("data/youtube_data.json", 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        for channel_name in youtube_urls:
            caption_data = dict()

            if channel_name not in youtube_urls:
                raise ValueError("유효한 채널 이름이 아닙니다.")

            channel_url = youtube_urls[channel_name]
            self.youtube_crawler.open_page(channel_url)
            self.youtube_crawler.scroll_until_end()

            shorts_items = self.youtube_crawler.get_all_shorts_elements()

            for item in shorts_items:
                title, link = self.youtube_crawler.get_title_and_link(item)

                if is_scraped(data, channel_name, title):
                    print(f"'{title}'은 이미 스크래핑된 제목입니다. 스킵합니다.")
                    break

                if title and link:
                    caption = self.youtube_parser.fetch_youtube_captions(link)
                    caption_data[title] = caption

            if caption_data:
                if channel_name in data:
                    updated_data = {**caption_data, **data[channel_name]}
                    print(updated_data)
                    data[channel_name] = updated_data
                else:
                    data[channel_name] = caption_data

        self.youtube_crawler.quit()

        with open("data/youtube_data.json", 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return data
