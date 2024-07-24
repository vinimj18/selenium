import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')

# Locators adentified by Selenium:
# Id, name, classname, Xpath, CSSSelector, linkText

driver.find_element(By.NAME, 'email').send_keys('vinimj_lixo18@gmail.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123456')
driver.find_element(By.ID, 'exampleCheck1').click()


time.sleep(5)
