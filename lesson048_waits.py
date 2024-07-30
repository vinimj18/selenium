import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

# The code will wait 5 seconds or less to execute the code (Max timeout)
# If the element is identified on the page, it will execute before the 5 seconds
driver.implicitly_wait(2)

driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('ber')

# keep the 'sleep' for find_elements, or the implicity wait can return an empty
# or incomplete list.
time.sleep(2)
items = driver.find_elements(By.XPATH, '//div[@class="products"]/div')
count_items = len(items)
assert count_items > 0

for item in items:
    item.find_element(By.XPATH, 'div/button').click()

driver.find_element(By.CSS_SELECTOR, '.cart-icon').click()
driver.find_element(By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]').click()

driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys(
    'rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()

# Explicit wait:
# This srep takes longer than the implicit wait. So we add an explicit wait just
# for this specific step
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located(
    (By.CSS_SELECTOR, '.promoInfo')))
print(driver.find_element(By.CSS_SELECTOR, '.promoInfo').text)
