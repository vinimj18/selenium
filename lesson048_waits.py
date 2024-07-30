import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('ber')
time.sleep(2)
items = driver.find_elements(By.XPATH, '//div[@class="products"]/div')
count_items = len(items)
assert count_items > 0

for item in items:
    item.find_element(By.XPATH, 'div/button').click()

driver.find_element(By.CSS_SELECTOR, '.cart-icon').click()
driver.find_element(By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]').click()

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys(
    'rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()
time.sleep(8)
print(driver.find_element(By.CSS_SELECTOR, '.promoInfo').text)
