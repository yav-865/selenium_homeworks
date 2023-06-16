import random
from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://localhost/litecart/en/create_account')
driver.implicitly_wait(10)
fake = Faker()
wait = WebDriverWait(driver, 20)

email = fake.email()
password = 'kasjGbc56'

driver.find_element(By.NAME, 'firstname').send_keys(fake.first_name())
driver.find_element(By.NAME, 'lastname').send_keys(fake.last_name())
driver.find_element(By.NAME, 'address1').send_keys('My address')
driver.find_element(By.NAME, 'city').send_keys(fake.city())
driver.find_element(By.NAME, 'postcode').send_keys(random.randint(10000,99999))
driver.find_element(By.CSS_SELECTOR, 'span.select2-selection__rendered').click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.select2-results__options')))
driver.find_element(By.XPATH,"//li[text()='United States']").click()
driver.find_element(By.NAME, 'email').send_keys(email)
driver.find_element(By.NAME, 'phone').send_keys('12324568')
driver.find_element(By.NAME, 'password').send_keys(password)
driver.find_element(By.NAME, 'confirmed_password').send_keys(password)
driver.find_element(By.NAME, 'create_account').click()
driver.implicitly_wait(20)
driver.find_element(By.LINK_TEXT, 'Logout').click()
driver.implicitly_wait(20)
driver.find_element(By.NAME, 'email').send_keys(email)
driver.find_element(By.NAME, 'password').send_keys(password)
driver.find_element(By.NAME, 'login').click()
driver.implicitly_wait(20)
driver.find_element(By.LINK_TEXT, 'Logout').click()



driver.close()
driver.quit()