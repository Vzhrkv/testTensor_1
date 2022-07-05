import time

import pytest
from pages.search_page import SearchPage
from selenium.webdriver.common.keys import Keys



@pytest.mark.usefixtures('setup')
class TestHomePage:

    def test_get_search_field(self):
        search_page = SearchPage(self.driver)
        assert search_page.get_search_field()

    def test_suggest_table(self):
        search_page = SearchPage(self.driver)
        search_page.input_text('Тензор')
        time.sleep(2)
        assert search_page.get_suggest_table()


    def test_get_search_results_links(self):
        search_page = SearchPage(self.driver)
        search_page.input_text('Тензор')
        search_page.press_key(Keys.ENTER)
        time.sleep(2)
        assert search_page.get_search_results_links()

    def test_check_the_site(self):
        search_page = SearchPage(self.driver)
        search_page.input_text('Тензор')
        search_page.press_key(Keys.ENTER)
        time.sleep(2)
        assert search_page.get_some_page_link(0) == 'https://tensor.ru/'
