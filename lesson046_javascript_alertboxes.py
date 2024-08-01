import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

name = 'Vinicius'
driver.find_element(By.ID, 'name').send_keys(name)
driver.find_element(By.ID, 'alertbtn').click()
alert = driver.switch_to.alert
alert_text = alert.text
alert.accept()  # Clicks on OK alert button
# alert.dismiss() # Clicks on CANCEL alert button

assert name in alert_text

time.sleep(3)
