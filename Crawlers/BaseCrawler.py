from selenium import webdriver
import time
from selenium.webdriver.edge.service import Service


class BaseCrawler:
    def __init__(self, driver_path):
        service = Service(executable_path=driver_path)
        self.driver = webdriver.Edge(service=service)

    def open_page(self, url):
        self.driver.get(url)
        time.sleep(2)

    def get_current_url(self):
        return self.driver.current_url

    def quit(self):
        self.driver.quit()