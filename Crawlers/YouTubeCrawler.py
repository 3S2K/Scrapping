from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Crawlers.BaseCrawler import BaseCrawler
import time
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import re
from selenium.common.exceptions import NoSuchElementException


class YouTubeCrawler(BaseCrawler):
    def get_all_shorts_elements(self):
        try:
            shorts_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "ytd-rich-item-renderer")))
            return shorts_elements
        except NoSuchElementException:
            print("숏츠 요소를 찾을 수 없습니다.")
            return []

    def get_title_and_link(self, item):
        try:
            # 링크 가져오기 (각 숏츠의 href 속성 추출)
            link_element = item.find_element(By.CSS_SELECTOR, "a[href^='/shorts']")
            link = link_element.get_attribute("href")
            # 제목 가져오기
            title_element = item.find_element(By.CSS_SELECTOR, "span.yt-core-attributed-string.yt-core-attributed-string--white-space-pre-wrap[role='text']")
            title = title_element.text if title_element else "제목 없음"

            return title, link
        except NoSuchElementException as e:
            print(f"요소를 찾지 못했습니다: {e}")
            return None, None

    def scroll_until_end(self):
        last_height = self.driver.execute_script("return document.documentElement.scrollHeight")

        while True:
            # 스크롤 내리기
            self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(3)  # 스크롤 후 로드 시간을 대기

            # 새로운 높이 계산
            new_height = self.driver.execute_script("return document.documentElement.scrollHeight")

            # 더 이상 새로운 콘텐츠가 없을 경우 종료
            if new_height == last_height:
                break
            last_height = new_height

    def avoid_advertisement(self):
        try:
            sponsor = self.driver.find_element(By.CLASS_NAME, "badge-shape-wiz__text")
            if sponsor in sponsor.text:
                self.click_next_shorts()
        except Exception as e:
            print(f"광고 건너뛰기 실패 또는 광고 없음 : {e}")




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