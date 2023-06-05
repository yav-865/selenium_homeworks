
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://localhost/litecart/')
driver.implicitly_wait(10)
cards = driver.find_elements(By.CSS_SELECTOR, "ul.listing-wrapper li")
for element in cards:
    sticker = element.find_elements(By.CSS_SELECTOR, "div.sticker")
    if len(sticker)!=1:
        print("У товара не один стикер")
    else:
        print("У товара один стикер")

driver.close()
driver.quit()