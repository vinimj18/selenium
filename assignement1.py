from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/loginpagePractise/')

driver.find_element(By.CSS_SELECTOR, '.blinkingText').click()

open_windows = driver.window_handles
driver.switch_to.window(open_windows[1])
email = driver.find_element(By.LINK_TEXT, 'mentor@rahulshettyacademy.com').text
driver.close()
driver.switch_to.window(open_windows[0])

driver.find_element(By.ID, 'username').send_keys(email)
driver.find_element(By.ID, 'password').send_keys('123456')
driver.find_element(By.ID, 'signInBtn').click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located(
    (By.CSS_SELECTOR, '.alert-danger')
))
login_alert = driver.find_element(By.CSS_SELECTOR, '.alert-danger').text

print(login_alert)
