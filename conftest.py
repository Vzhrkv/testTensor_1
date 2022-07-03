import pytest
from selenium import webdriver


@pytest.fixture
def get_webdriver():
    path = '/home/vladimir/Desktop/testTensor/chromedriver/chromedriver'
    driver = webdriver.Chrome(executable_path=path)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.yandex.ru/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()