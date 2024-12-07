from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Crawlers.BaseCrawler import BaseCrawler
import time


class NewsCrawler(BaseCrawler):
    def close_popup(self):
        try:
            self.driver.execute_script(
                "document.querySelector('button[data-name=\\'popup-dismiss\\'][data-type=\\'close\\']').click();"
            )
        except Exception as e:
            print(f"팝업 없음: {e}")

    def maximize_window(self):
        self.driver.maximize_window()

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 300);")

    def move_next_slide(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[class='swiper-next'][aria-label='Next slide']")
            )
        ).click()

    def get_aria_titles(self, index: int) -> str:
        aria_tab = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[class='swiper-wrapper tab-link tab01']")
            )
        )
        aria_index = aria_tab.find_element(
            By.CSS_SELECTOR, f"div[data-idx='{index}']"
        )
        aria_index.click()
        aria_title = aria_index.find_element(
            By.CSS_SELECTOR, "span[class='issue-topic-txt']"
        )
        time.sleep(4)
        return aria_title.text

    def get_main_news(self, index_dict: dict):
        news_main = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "news-main"))
        )
        news_main_title = news_main.find_element(By.CSS_SELECTOR, "strong[title='팝업창 열림']")
        news_main_title.click()
        news_contents = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "news-view-body")))
        index_dict[news_main_title.text] = news_contents.text
        time.sleep(2)
        self.close_news()

    def close_news(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "button[class='btn btn-round btn-wh']")
                )
            ).click()
        except Exception as e:
            print(f"닫기버튼 없음: {e}")

    def get_sub_news(self, index_dict: dict):
        try:
            news_lst = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul[class='news-lst']"))
            )
            news_lst = news_lst.find_elements(By.TAG_NAME, "li")
            for new in news_lst:
                title = new.find_element(By.CSS_SELECTOR, "strong[class='title']")
                title.click()
                news_contents = WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "news-view-body")))
                index_dict[title.text] = news_contents.text
                time.sleep(2)
                self.close_news()
        except Exception as e:
            print(f"news 없음: {e}")
