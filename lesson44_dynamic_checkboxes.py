import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

time.sleep(2)
