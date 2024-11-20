from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Crawlers.BaseCrawler import BaseCrawler
import time


class NewsCrawler(BaseCrawler):
    def open_news_site(self, url):
        self.open_page(url)
        time.sleep(2)


    def get_news_title(self):
        # 뉴스 페이지에서 타이틀을 가져오는 로직을 여기에 작성하세요.
        pass
