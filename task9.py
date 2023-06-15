from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://localhost/litecart/admin/')
driver.implicitly_wait(10)
username = driver.find_element(By.NAME, "username").send_keys("admin")
password = driver.find_element(By.NAME, "password").send_keys("admin")
login_button = driver.find_element(By.NAME, "login").click()
driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')



driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
list_zones = driver.find_elements(By.CSS_SELECTOR,"tr.row td:nth-child(3) a")

zones_links = []
for element in list_zones:
    zones_links.append(element.text)

for root_link in zones_links:
    driver.find_element(By.LINK_TEXT, root_link).click()
    sub_elements = driver.find_elements(By.CSS_SELECTOR, "[name=form_geo_zone] td:nth-child(3) option[selected]")
    text = []
    for sub_element in sub_elements:
        text.append(sub_element.text)

    if text == sorted(text):
        print("Зоны расположены по алфавиту")
    else:
        print("Зоны расположены не по алфавиту")
    driver.back()

driver.close()
driver.quit()