from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from .locators import Locator
from .base_page import BasePage

class SearchPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def get_search_field(self):
        return self.is_present(*Locator.SEARCH_PANEL)

    def get_suggest_table(self):
        return self.is_present(*Locator.SUGGEST_TABLE)

    def input_text(self, word):
        '''Input text in search field'''
        self.get_search_field().send_keys(word)

    def press_key(self, key):
        '''send Keys from selenium.webdriver.common.keys'''
        self.get_search_field().send_keys(key)


    def get_search_results(self):
        return self.are_visible(*Locator.SEARCH_RESULT_PANEL)

    def get_search_results_links(self) -> list:
        links = self.get_search_results()
        return [link.get_dom_attribute('href') for link in links]

    def get_some_page_link(self, number: int):
        link = self.get_search_results_links()
        return link[number]