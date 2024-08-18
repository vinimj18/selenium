import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)

# Getting a part of the locator
# CSS Selector = a[href*="shop"]
# XPath = //a[contains(@href, "shop")]

driver.find_element(By.CSS_SELECTOR, 'a[href*="shop"]').click()
products = driver.find_elements(By.XPATH, '//div[@class="card h-100"]')

for product in products:
    product_name = product.find_element(By.XPATH, 'div/h4/a').text
    if product_name == 'Blackberry':
        product.find_element(By.XPATH, 'div/button').click()
        break

driver.find_element(By.CSS_SELECTOR, 'a[class*="btn-primary"]').click()
driver.find_element(By.CLASS_NAME, 'btn-success').click()

driver.find_element(By.ID, 'country').send_keys('it')

wait = WebDriverWait(driver, 12)
wait.until(
    expected_conditions.presence_of_element_located((By.LINK_TEXT, 'Italy')))
driver.find_element(By.LINK_TEXT, 'Italy').click()
driver.find_element(
    By.XPATH, '//div[@class="checkbox checkbox-primary"]').click()
driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
success_message = driver.find_element(By.CLASS_NAME, 'alert-success').text

assert 'Success! Thank you!' in success_message
print('Success')
