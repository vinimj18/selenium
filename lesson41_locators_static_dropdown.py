import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')

# Selecting from static dropdowns
dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown.select_by_visible_text('Female')
time.sleep(1)
dropdown.select_by_index(0)
time.sleep(1)
dropdown.select_by_index(1)


time.sleep(5)
