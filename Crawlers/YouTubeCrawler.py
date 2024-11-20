from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Crawlers.BaseCrawler import BaseCrawler
import time
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import re


class YouTubeCrawler(BaseCrawler):
    def open_shorts_channel(self, url):
        self.open_page(url)
        time.sleep(2)

    def click_first_shorts(self):
        first_shorts = self.driver.find_element(By.CSS_SELECTOR, 'a[href^="/shorts"]:nth-child(1)')
        first_shorts.click()
        time.sleep(2)

    def get_current_title(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "yt-shorts-video-title-view-model"))
            )
            time.sleep(1)
            title_element = self.driver.find_element(By.TAG_NAME, "yt-shorts-video-title-view-model")
            return title_element.text.strip() if title_element else "제목 없음"
        except Exception as e:
            print(f"제목 가져오기 실패: {e}")
            return "제목 없음"

    def click_next_shorts(self):
        try:
            current_url = self.get_current_url()
            next_button = self.driver.find_element(By.ID, "navigation-button-down")
            next_button.click()
            WebDriverWait(self.driver, 10).until(
                EC.url_changes(current_url)
            )
            time.sleep(2)
        except Exception as e:
            print(f"다음 버튼 클릭 실패: {e}")


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



