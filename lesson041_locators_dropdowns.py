import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

# Getting static dropdowns

# driver = webdriver.Chrome()
# driver.get('https://rahulshettyacademy.com/angularpractice/')

# # Selecting from static dropdowns
# dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
# dropdown.select_by_visible_text('Female')
# time.sleep(1)
# dropdown.select_by_index(0)
# time.sleep(1)
# dropdown.select_by_index(1)
# time.sleep(5)

# Getting dynamic dropdowns

driver2 = webdriver.Chrome()
driver2.get('https://rahulshettyacademy.com/dropdownsPractise/')
driver2.find_element(By.ID, 'autosuggest').send_keys('ind')
time.sleep(2)
countries = driver2.find_elements(
    By.CSS_SELECTOR, 'li[class="ui-menu-item"] a')

for country in countries:
    if country.text == 'India':
        country.click()
        break

# Getting a text inserted via script

# The code below won't work because if the text was inserted via script
# method .text won't work.
# print(driver2.find_element(By.ID, 'autosuggest').text)

# Use get.attribute() instead
assert driver2.find_element(
    By.ID, 'autosuggest').get_attribute('value') == 'India'

time.sleep(2)
