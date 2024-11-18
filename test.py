from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
from info import urls
from selenium.webdriver.edge.service import Service


class YouTubeCrawler:
    def __init__(self, driver_path):
        service = Service(executable_path=driver_path)
        self.driver = webdriver.Edge(service=service)

    def open_shorts_channel(self, url):
        self.driver.get(url)
        time.sleep(2)


    def click_first_shorts(self):
        first_shorts = self.driver.find_element(By.CSS_SELECTOR, 'a[href^="/shorts"]:nth-child(1)')
        first_shorts.click()
        time.sleep(2)

    def get_current_url(self):
        return self.driver.current_url

    def get_current_title(self):
        return self.driver.find_element(By.TAG_NAME, "yt-shorts-video-title-view-model").text

    def click_next_shorts(self):
        try:
            next_button = self.driver.find_element(By.ID, "navigation-button-down")
            next_button.click()
            time.sleep(2)
        except Exception as e:
            print(f"다음 버튼 클릭 실패: {e}")

    def quit(self):
        self.driver.quit()


class YouTubeTranscriptExtractor:
    @staticmethod
    def get_youtube_video_id(url):
        video_id_match = re.search(r"(?:v=|youtu\.be/|embed/|shorts/)([a-zA-Z0-9_-]{11})", url)
        if video_id_match:
            return video_id_match.group(1)
        else:
            raise ValueError("유효한 YouTube URL이 아닙니다.")

    @staticmethod
    def fetch_youtube_captions(url):
        try:
            video_id = YouTubeTranscriptExtractor.get_youtube_video_id(url)
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

            try:
                transcript = transcript_list.find_transcript(['ko', 'en'])
            except:
                transcript = transcript_list.find_manually_created_transcript(['en'])

            captions = transcript.fetch()

            # 자막 형식 변환
            formatter = TextFormatter()
            text_captions = formatter.format_transcript(captions)
            return text_captions

        except Exception as e:
            return f"자막을 가져오는 중 오류 발생: {e}"


class YouTubeScraper:
    def __init__(self, driver_path):
        self.crawler = YouTubeCrawler(driver_path)
        self.transcript_extractor = YouTubeTranscriptExtractor()

    def scrape_shorts_captions(self, channel_name, num_shorts=2):
        if channel_name not in urls:
            raise ValueError("유효한 채널 이름이 아닙니다.")

        channel_url = urls[channel_name]
        self.crawler.open_shorts_channel(channel_url)
        self.crawler.click_first_shorts()

        captions_data = {}

        for i in range(num_shorts):
            current_url = self.crawler.get_current_url()
            captions = self.transcript_extractor.fetch_youtube_captions(current_url)
            captions_data[self.crawler.get_current_title()] = captions
            time.sleep(3)
            self.crawler.click_next_shorts()

        self.crawler.quit()
        return captions_data


if __name__ == "__main__":
    driver_path = "C:\\Users\\home\\Documents\\edgedriver_win64\\msedgedriver.exe"
    scraper = YouTubeScraper(driver_path)
    channel_name = "썰송이"
    captions = scraper.scrape_shorts_captions(channel_name)
    print("수집된 자막 데이터:", captions)
