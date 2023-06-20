from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import random
import string
import os
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)
driver.get('http://localhost/litecart/admin/')
driver.implicitly_wait(10)
username = driver.find_element(By.NAME, "username").send_keys("admin")
password = driver.find_element(By.NAME, "password").send_keys("admin")
login_button = driver.find_element(By.NAME, "login").click()
driver.get('http://localhost/litecart/admin/?app=catalog&doc=catalog')
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT, 'Add New Product').click()

name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 8))


driver.find_element(By.NAME, 'name[en]').send_keys(name)
driver.find_element(By.NAME, 'code').send_keys('123456')

categories = driver.find_elements(By.CSS_SELECTOR, "input[name='categories[]']")
for category in categories:
    category.click()

groups = driver.find_elements(By.CSS_SELECTOR, "input[name='product_groups[]']")
for group in groups:
    group.click()

driver.find_element(By.NAME, 'quantity').send_keys('15')
driver.find_element(By.CSS_SELECTOR, "input[name='new_images[]']").send_keys(os.path.abspath('pic.jpg'))
driver.find_element(By.NAME, 'date_valid_from').send_keys('15062022')
driver.find_element(By.NAME, 'date_valid_to').send_keys('15062023')
driver.find_element(By.LINK_TEXT, 'Information').click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name="manufacturer_id"]')))
driver.find_element(By.NAME, 'manufacturer_id').click()
driver.find_element(By.CSS_SELECTOR, "select[name='manufacturer_id'] option[value='1']").click()
driver.find_element(By.NAME, 'keywords').send_keys('word')
driver.find_element(By.NAME, 'short_description[en]').send_keys('description')
driver.find_element(By.NAME, 'description[en]').send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ullamcorper libero at ipsum consequat commodo.')
driver.find_element(By.NAME, 'head_title[en]').send_keys('some title')
driver.find_element(By.NAME, 'meta_description[en]').send_keys('meta')
driver.find_element(By.LINK_TEXT, 'Prices').click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name="purchase_price"]')))
driver.find_element(By.NAME, 'purchase_price').send_keys('123')
driver.find_element(By.NAME, 'purchase_price_currency_code').click()
driver.find_element(By.CSS_SELECTOR, "select[name='purchase_price_currency_code'] option[value='USD']").click()



driver.find_element(By.NAME, 'prices[USD]').send_keys('123')
driver.find_element(By.NAME, 'prices[EUR]').send_keys('321')
driver.find_element(By.NAME, 'save').click()
driver.implicitly_wait(10)
names = driver.find_elements(By.CSS_SELECTOR, 'tr.row td:nth-child(3) a')
names2 = []

for element in names:
    n = element.get_attribute("textContent")
    names2.append(n)


if names2.count(name):
    print('Товар добавлен!')
else:
    print('Ошибка :(')



driver.close()
driver.quit()
