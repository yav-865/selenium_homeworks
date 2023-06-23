from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)
driver.get('http://localhost/litecart/')
for i in range(3):
    driver.find_element(By.CSS_SELECTOR,'div.content li:first-child a.link').click()
    driver.implicitly_wait(20)
    cart = driver.find_element(By.CSS_SELECTOR, 'span.quantity')
    count = int(cart.get_attribute("textContent"))+1
    driver.find_element(By.NAME, 'add_cart_product').click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"),str(count)))
    driver.back()
driver.find_element(By.LINK_TEXT, 'Checkout »').click()
list = driver.find_elements(By.CSS_SELECTOR, 'li.item')
for item in list:
    driver.find_element(By.NAME, 'remove_cart_item').click()
    wait.until(EC.staleness_of(driver.find_element(By.CSS_SELECTOR, 'td.item')))
driver.close()
driver.quit()

