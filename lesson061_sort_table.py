import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

veggie_table_list = []

driver.find_element(By.XPATH, '//span[text()="Veg/fruit name"]').click()
veggies = driver.find_elements(By.XPATH, '//tr/td[1]')
for veggie in veggies:
    veggie_table_list.append(veggie.text)

veggie_table_list_sorted = veggie_table_list.copy()
veggie_table_list_sorted.sort()

assert veggie_table_list == veggie_table_list_sorted
