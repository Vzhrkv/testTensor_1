from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    """Base class for base actions"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, 1)

    def is_present(self, by_what, value) -> WebElement:
        """function for find element on page"""
        return self.wait.until(EC.presence_of_element_located((by_what, value)))

    def are_visible(self, by_what, value):
        return self.wait.until(EC.visibility_of_all_elements_located((by_what, value)))
