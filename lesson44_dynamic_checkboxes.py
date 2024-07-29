import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# Use this if you don't know the order, or if the options order can change.

checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break


# Use this if you know that the options will always be in the same order.

radiobuttons = driver.find_elements(By.CSS_SELECTOR, '.radioButton')
radiobuttons[2].click()
assert radiobuttons[2].is_selected()


# Check if an element is displayed on the screen

assert driver.find_element(By.ID, 'displayed-text').is_displayed()
driver.find_element(By.ID, 'hide-textbox').click()
assert not driver.find_element(By.ID, 'displayed-text').is_displayed()


time.sleep(2)
