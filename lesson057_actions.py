from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, 'mousehover')).perform()
action.move_to_element(driver.find_element(
    By.LINK_TEXT, 'Reload')).click().perform()

# Other Actions examples
# action.double_click()
# action.drag_and_drop()
# action.context_click() -> right click
