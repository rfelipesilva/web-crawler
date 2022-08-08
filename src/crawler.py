# @author: Renan Silva
#? @github: https://github.com/rfelipesilva
#! Python3.8

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# USE ALWAYS LAST DRIVER VERSION
driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.canaldapeca.com.br/'

driver.get(url)
time.sleep(3)

# START WITH "MOTOR" SECTION AND GET FIRST PAGE DATA
driver.find_element(By.XPATH, '//*[@id="header-div"]/div[2]/nav/div/div/div/ul/li[1]/span/a').click()
time.sleep(3)

products = driver.find_elements(By.CLASS_NAME, 'y-item-wrapper-showcase')

print('MOTOR')
for product in products:
    product_name = product.find_element(By.CLASS_NAME, 'produto-nome').text
    product_image = product.find_element(By.TAG_NAME, 'img').get_attribute('src')
    product_code = product.find_element(By.CLASS_NAME, 'produto-mfrPartCode').text
    product_application = product.find_element(By.CLASS_NAME, 'application_value').text

    print(product_name)
    print(product_image)
    print(product_code)
    print(product_application)
    print('--'*30)

# SWITCH TO "SUSPENSÃO" PAGE AND GET FIRST PAGE DATA
driver.find_element(By.XPATH, '//*[@id="header-div"]/div[2]/nav/div/div/div/ul/li[2]/span/a').click()

products = driver.find_elements(By.CLASS_NAME, 'y-item-wrapper-showcase')
time.sleep(3)

print('SUSPENSÃO')
for product in products:
    product_name = product.find_element(By.CLASS_NAME, 'produto-nome').text
    product_image = product.find_element(By.TAG_NAME, 'img').get_attribute('src')
    product_code = product.find_element(By.CLASS_NAME, 'produto-mfrPartCode').text
    product_application = product.find_element(By.CLASS_NAME, 'application_value').text

    print(product_name)
    print(product_image)
    print(product_code)
    print(product_application)
    print('--'*30)

driver.quit()