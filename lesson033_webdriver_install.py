import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Manual webdriver installation
# If using a older version of Chrome, download the webdriver from:
# https://developer.chrome.com/docs/chromedriver/downloads?hl=pt-br
# Then do the following:

# service_obj = Service('path_in_which_you_installed_chrome_driver/chromedriver')
# driver = webdriver.Chrome(service=service_obj)


# Automatic Chrome driver service
driver = webdriver.Chrome()
driver.get('https://github.com/vinimj18')


time.sleep(3)
