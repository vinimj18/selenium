import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://github.com/vinimj18')
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(3)

# To test in another browser just change the webdriver service name.
# driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Edge()
# driver = webdriver.Safari()
