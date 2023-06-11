from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://localhost/litecart/admin/')
driver.implicitly_wait(10)
username = driver.find_element(By.NAME, "username").send_keys("admin")
password = driver.find_element(By.NAME, "password").send_keys("admin")
login_button = driver.find_element(By.NAME, "login").click()
driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')

# проверяет, что страны расположены в алфавитном порядке

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

# для тех стран, у которых количество зон отлично от нуля -- открывает страницу этой страны и там проверяет, что геозоны расположены в алфавитном порядке

row_list = driver.find_elements(By.CSS_SELECTOR, "table.dataTable tr.row")
for row in row_list:
    zone = row.find_element(By.CSS_SELECTOR, "td:nth-child(6)")
    value = int(zone.get_attribute("textContent"))
    if value !=0:
        country_zone = row.find_element(By.CSS_SELECTOR, "td:nth-child(5) a")
        country_zone.click()
        driver.implicitly_wait(8)
        zone_list = driver.find_elements(By.CSS_SELECTOR, "table#table-zones input[name*=name]")
        zone_list2=[]
        for z in zone_list:
            zone_name = z.get_attribute("value")
            if zone_name!='':
                zone_list2.append(zone_name)
        sorted_zones = sorted(zone_list2)
        if sorted_zones == zone_list2:
            print('Зоны расположены по алфавиту')
        else:
            print("Зоны расположены не по алфавиту")
        driver.back()

driver.close()
driver.quit()
