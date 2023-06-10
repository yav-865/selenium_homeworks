from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://localhost/litecart/admin/')
driver.implicitly_wait(10)
username = driver.find_element(By.NAME, "username").send_keys("admin")
password = driver.find_element(By.NAME, "password").send_keys("admin")
login_button = driver.find_element(By.NAME, "login").click()

nav_list = driver.find_elements(By.CSS_SELECTOR, "#box-apps-menu li")

for i in range(1,len(nav_list)+1):
    driver.find_element(By.CSS_SELECTOR, f"#box-apps-menu  li:nth-child({i})").click()
    sub_elements = driver.find_elements(By.CSS_SELECTOR, f"#box-apps-menu li:nth-child({i}) li")
    if len(sub_elements) != 0:
        for a in range(1,len(sub_elements)+1):
            driver.find_element(By.CSS_SELECTOR, f"#box-apps-menu >li:nth-child({i}) ul li:nth-child({a})").click()
            driver.find_element(By.CSS_SELECTOR, "h1")
driver.close()
driver.quit()

















