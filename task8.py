from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)
driver.get('http://localhost/litecart/admin/')
driver.implicitly_wait(10)
username = driver.find_element(By.NAME, "username").send_keys("admin")
password = driver.find_element(By.NAME, "password").send_keys("admin")
login_button = driver.find_element(By.NAME, "login").click()
driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')
i = 0

country_list = driver.find_elements(By.CSS_SELECTOR, "table.dataTable tr.row td:nth-child(5) a")
country_list2 = []

for element in country_list:
    country = element.get_attribute("textContent")
    country_list2.append(country)

sort_country_list = sorted(country_list2)

if sort_country_list == country_list2:
    print('Элементы расположены по алфавиту')
else:
    print("Элементы расположены не по алфавиту")


zones = driver.find_elements(By.CSS_SELECTOR,"[name=countries_form] td:nth-child(6)")
zone_links = []
for zone in zones:
    zone_links.append(zone.text)


for link in country_list2:
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name="disable"]')))
    if int(zone_links[i]) != 0:
        driver.find_element(By.LINK_TEXT,(link)).click()
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        sub_elements = driver.find_elements(By.CSS_SELECTOR,"form td:nth-child(3)")
        sub_text = []
        for sub_element in sub_elements:
            if sub_element.text != "":
                sub_text.append(sub_element.text)

        if sub_text == sorted(sub_text):
            print("Зоны расположены по алфавиту")
        else:
            print("Зоны расположены не по алфавиту")

        driver.back()
    i += 1

driver.close()
driver.quit()
