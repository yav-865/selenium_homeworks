import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome("C:\chromedriver")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get('https://ya.ru/')
    driver.implicitly_wait(10)

