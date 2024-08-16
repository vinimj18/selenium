import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')

# Locators identified by Selenium:
# Id, name, classname, Xpath, CSSSelector, linkText

driver.find_element(By.NAME, 'email').send_keys('vinimj_lixo18@gmail.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123456')
driver.find_element(By.ID, 'exampleCheck1').click()

# Creating an Xpath -> //tagname[@attribute='value']
# Creating an CSSSelector -> tagname[attribute='value']
driver.find_element(
    By.XPATH, '(//input[@name="name"])[1]').send_keys('Vinicius')
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()
message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)

driver.find_element(
    By.XPATH, '(//input[@name="name"])[2]').clear()

assert 'Success' in message

time.sleep(5)
