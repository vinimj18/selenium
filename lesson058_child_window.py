from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/windows')

driver.find_element(By.LINK_TEXT, 'Click Here').click()
open_window = driver.window_handles

driver.switch_to.window(open_window[1])
print(driver.find_element(By.CSS_SELECTOR, 'h3').text)
driver.close()
driver.switch_to.window(open_window[0])
assert 'Opening a new window' == driver.find_element(
    By.CSS_SELECTOR, 'h3').text
