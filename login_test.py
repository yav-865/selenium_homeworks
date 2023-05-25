import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome("C:\chromedriver")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get('http://localhost/litecart/admin/')
    driver.implicitly_wait(10)
    username = driver.find_element(By.NAME, "username")
    username.send_keys("admin")
    password = driver.find_element(By.NAME, "password")
    password.send_keys("admin")
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()









