import time
from Crawlers.NewsCrawler import NewsCrawler
import copy


class NewsScraper:
    def __init__(self, driver_path: str):
        self.news_crawler = NewsCrawler(driver_path)
        self.final_dict = dict()

    def scrape_news(self, news_url: str) -> dict:
        self.news_crawler.open_page(news_url)
        self.news_crawler.close_popup()
        self.news_crawler.maximize_window()
        self.news_crawler.scroll_down()
        time.sleep(2)
        for index in range(10):
            index_dict = dict()
            if index == 5:
                self.news_crawler.move_next_slide()
            news_aria_title = self.news_crawler.get_aria_titles(index)
            time.sleep(2)
            self.news_crawler.get_main_news(index_dict)
            time.sleep(2)
            self.news_crawler.get_sub_news(index_dict)
            self.final_dict[news_aria_title] = copy.deepcopy(index_dict)
        self.news_crawler.quit()
        return self.final_dict
