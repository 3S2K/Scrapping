from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Crawlers.BaseCrawler import BaseCrawler
import time


class NewsCrawler(BaseCrawler):
    def __init__(self, driver_path):
        super().__init__(driver_path)
        self.news_dict = dict()

    def close_popup(self):
        try:
            self.driver.execute_script("document.querySelector('button[data-name=\\'popup-dismiss\\'][data-type=\\'close\\']').click();")
        except Exception as e:
            print(f"팝업 없음: {e}")

    def maximize_window(self):
        self.driver.maximize_window()

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 300);")

    def move_next_slide(self):
        self.driver.find_element(By.CSS_SELECTOR, "div[class='swiper-next'][aria-label='Next slide']").click()

    def get_aria_titles(self, index):
        aria_tab = self.driver.find_element(By.CSS_SELECTOR, "div[class='swiper-wrapper tab-link tab01']")
        aria_index = aria_tab.find_element(By.CSS_SELECTOR, f"div[data-idx='{index}']")
        aria_title = aria_index.find_element(By.CSS_SELECTOR, "span[class='issue-topic-txt']")
        aria_title.click()
        time.sleep(4)
        return aria_title.text

    def get_main_news(self):
        news_main = self.driver.find_element(By.CLASS_NAME, "news-main")
        news_main_title = news_main.find_element(By.CSS_SELECTOR, "strong[class='title']")
        news_main_title.click()
        time.sleep(2)
        news_contents = self.driver.find_element(By.CLASS_NAME, "news-view-body")
        self.news_dict[news_main_title.text] = news_contents.text
        self.close_news()

    def close_news(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-round btn-wh']").click()
        except Exception as e:
            print(f"닫기버튼 없음: {e}")

    def get_sub_news(self):
        try:
            news_lst = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[class = 'news-lst']")))
            news_lst = news_lst.find_elements(By.TAG_NAME, "li")
            for new in news_lst:
                title = new.find_element(By.CSS_SELECTOR, "strong[class = 'title']")
                title.click()
                time.sleep(2)
                news_contents = self.driver.find_element(By.CLASS_NAME, "news-view-body")
                self.news_dict[title.text] = news_contents.text
                self.close_news()

        except Exception as e:
            print(f"news 없음: {e}")