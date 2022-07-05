from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class SearchPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.search_panel = '//*[@id="text"]'
        self.suggest_table = '/html/body/div[2]'
        self.search_result_table = '#search-result > li > div > div > div > a'

    def get_search_field(self):
        return self.is_present(By.XPATH, self.search_panel)

    def get_suggest_table(self):
        return self.is_present(By.XPATH, self.suggest_table)

    def input_text(self, word):
        '''Input text in search field'''
        self.get_search_field().send_keys(word)

    def press_key(self, key):
        '''send Keys from selenium.webdriver.common.keys'''
        self.get_search_field().send_keys(key)


    def get_search_results(self):
        return self.are_visible(By.CSS_SELECTOR, self.search_result_table)

    def get_search_results_links(self) -> list:
        links = self.get_search_results()
        return [link.get_dom_attribute('href') for link in links]

    def get_some_page_link(self, number: int):
        link = self.get_search_results_links()
        return link[number]