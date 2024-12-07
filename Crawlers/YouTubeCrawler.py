from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Crawlers.BaseCrawler import BaseCrawler
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement


class YouTubeCrawler(BaseCrawler):
    def get_all_shorts_elements(self) -> list:
        try:
            shorts_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "ytd-rich-item-renderer")))
            return shorts_elements
        except NoSuchElementException:
            print("숏츠 요소를 찾을 수 없습니다.")
            return []

    def get_title_and_link(self, item: WebElement) -> tuple:
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



