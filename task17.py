from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://localhost/litecart/admin/')
username = driver.find_element(By.NAME, "username").send_keys("admin")
password = driver.find_element(By.NAME, "password").send_keys("admin")
login_button = driver.find_element(By.NAME, "login").click()
driver.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1')
links = driver.find_elements(By.CSS_SELECTOR, 'tr.row td:nth-child(3) a')
logs = []
list = []
for link in links:
    list.append(link.text)
del list[0:3]
for a in list:
    driver.find_element(By.LINK_TEXT, a).click()
    driver.implicitly_wait(20)
    log = driver.get_log("browser")
    logs.append(log)
    driver.back()
print(logs)
driver.quit()