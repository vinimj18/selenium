from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/iframe')

driver.switch_to.frame('mce_0_ifr')
print(driver.find_element(By.ID, 'tinymce').text)
driver.find_element(By.ID, 'tinymce').send_keys('My name is Vinicius')

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, 'h3').text)
