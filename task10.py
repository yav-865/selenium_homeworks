import re
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://localhost/litecart/')
driver.implicitly_wait(10)

# main

name_main = driver.find_element(By.CSS_SELECTOR, 'div#box-campaigns div.content div.name').text
price_old_main = driver.find_element(By.CSS_SELECTOR, 'div#box-campaigns div.content s.regular-price').text
price_new_main = driver.find_element(By.CSS_SELECTOR, 'div#box-campaigns div.content strong.campaign-price').text
color_old_main = driver.find_element(By.CSS_SELECTOR, 'div#box-campaigns div.content s.regular-price').value_of_css_property("color")
style_old_main = driver.find_element(By.CSS_SELECTOR, 'div#box-campaigns div.content s.regular-price').value_of_css_property("text-decoration-line")
color_new_main = driver.find_element(By.CSS_SELECTOR, 'div#box-campaigns div.content strong.campaign-price').value_of_css_property("color")
style_new_main = driver.find_element(By.CSS_SELECTOR, 'div#box-campaigns div.content strong.campaign-price').value_of_css_property("font-weight")
font_old_main = driver.find_element(By.CSS_SELECTOR, 'div#box-campaigns div.content s.regular-price').value_of_css_property("font-size")
font_new_main = driver.find_element(By.CSS_SELECTOR, 'div#box-campaigns div.content strong.campaign-price').value_of_css_property("font-size")
driver.find_element(By.CSS_SELECTOR, 'div#box-campaigns a.link').click()
# card
name_card = driver.find_element(By.CSS_SELECTOR, 'h1.title').text
price_old_card = driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper s.regular-price').text
price_new_card = driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper strong.campaign-price').text
color_old_card = driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper s.regular-price').value_of_css_property("color")
style_old_card = driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper s.regular-price').value_of_css_property("text-decoration-line")
color_new_card = driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper strong.campaign-price').value_of_css_property("color")
style_new_card = driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper strong.campaign-price').value_of_css_property("font-weight")
font_old_card = driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper s.regular-price').value_of_css_property("font-size")
font_new_card = driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper strong.campaign-price').value_of_css_property("font-size")


# а) на главной странице и на странице товара совпадает текст названия товара

if name_main==name_card:
    print('Названия совпадают')
else:
    print('Названия не совпадают')


# б) на главной странице и на странице товара совпадают цены (обычная и акционная)

if price_old_main==price_old_card:
    print('Неакционные цены совпадают')
else:
    print('Неакционные  цены  не совпадают')

if price_new_main==price_new_card:
    print('Акционные цены совпадают')
else:
    print('Акционные цены не совпадают')

# обычная цена зачёркнутая и серая (можно считать, что "серый" цвет это такой, у которого в RGBa представлении одинаковые значения для каналов R, G и B)

if style_old_main =='line-through':
    print('Обычная цена на главной зачеркнута')
else:
    print('Обычная цена на главной не зачеркнута')

if style_old_card =='line-through':
    print('Обычная цена в карточке зачеркнута')
else:
    print('Обычная цена в карточке не зачеркнута')
    

match = re.findall(r'\d+', color_old_main)
r = match[0]
g = match[1]
b = match[2]

if r==g and g==b and r==b:
    print('Обычная цена на главной серая')
else:
    print('Обычная цена на главной не серая')

match2 = re.findall(r'\d+', color_old_card)
r2 = match2[0]
g2 = match2[1]
b2 = match2[2]

if r2==g2 and g2==b2 and r2==b2:
    print('Обычная цена в карточке серая')
else:
    print('Обычная цена в карточке не серая')
    
if int(style_new_main) >=700:
    print('Акционная цена на главной жирная')
else:
    print('Акционная цена на главной не жирная')

if int(style_new_card) >=700:
    print('Акционная цена в карточке жирная')
else:
    print('Акционная цена в карточке не жирная')

# г) акционная жирная и красная (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы G и B имеют нулевые значения)
match3 = re.findall(r'\d+', color_new_main)
r3 = int(match3[0])
g3 = int(match3[1])
b3 = int(match3[2])


if g3==0 and b3==0:
    print('Акционная цена на главной красная')
else:
    print('Акционная цена на главной не красная')

match4 = re.findall(r'\d+', color_new_card)
r4 = int(match4[0])
g4 = int(match4[1])
b4 = int(match4[2])

if g4==0 and b4==0:
    print('Акционная цена в карточке красная')
else:
    print('Акционная цена в карточке красная')

# д) акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)
mfont_old = re.findall(r'\d+', font_old_main)
mfont_new = re.findall(r'\d+', font_new_main)

if mfont_old[0]<mfont_new[0]:
    print('Акционная цена на главной крупнее')
else:
    print('Обычная цена на главной крупнее')

cfont_old = re.findall(r'\d+', font_old_card)
cfont_new = re.findall(r'\d+', font_new_card)

if int(cfont_old[0]) < int(cfont_new[0]):
    print('Акционная цена в карточке крупнее')
else:
    print('Обычная цена в карточке крупнее')

driver.close()
driver.quit()