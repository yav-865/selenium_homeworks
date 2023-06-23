from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 20)
driver.get('http://localhost/litecart/admin/')
username = driver.find_element(By.NAME, "username").send_keys("admin")
password = driver.find_element(By.NAME, "password").send_keys("admin")
login_button = driver.find_element(By.NAME, "login").click()
driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')
driver.find_element(By.LINK_TEXT,'Add New Country').click()
links = driver.find_elements(By.CSS_SELECTOR, 'form table a[target="_blank"')
main_window = driver.current_window_handle
new_window = []
for i in range(len(links)):
    links[i].click()
    new_window = driver.window_handles
    new_window.remove(main_window)
    wait.until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(new_window[0])
    driver.close()
    driver.switch_to.window(main_window)
driver.quit()
