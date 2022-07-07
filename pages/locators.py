from selenium.webdriver.common.by import By

class Locator:

    SEARCH_PANEL = (By.XPATH, '//*[@id="text"]')
    SUGGEST_TABLE = (By.XPATH, '/html/body/div[2]')
    SEARCH_RESULT_PANEL = (By.CSS_SELECTOR, '#search-result > li > div > div > div > a')
