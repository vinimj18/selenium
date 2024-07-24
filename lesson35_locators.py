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

# Creating an Xpath -> //tagname[@attribute='value']
# Creating an CSSSelector -> tagname[attribute='value']
driver.find_element(
    By.CSS_SELECTOR, "input[name='name']").send_keys('Vinicius')
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)

assert 'Success' in message

time.sleep(5)
