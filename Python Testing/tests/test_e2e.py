# type: ignore

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from utilities.base_class import BaseClass
from page_objects.home_page import HomePage


class TestOne(BaseClass):
    def test_e2e(self):

        home_page = HomePage(self.driver)
        self.driver.implicitly_wait(5)

        home_page.shop_items().click()
        # self.driver.find_element(By.CSS_SELECTOR, 'a[href*="shop"]').click()
        products = self.driver.find_elements(
            By.XPATH, '//div[@class="card h-100"]')

        for product in products:
            product_name = product.find_element(By.XPATH, 'div/h4/a').text
            if product_name == 'Blackberry':
                product.find_element(By.XPATH, 'div/button').click()
                break

        self.driver.find_element(
            By.CSS_SELECTOR, 'a[class*="btn-primary"]').click()
        self.driver.find_element(By.CLASS_NAME, 'btn-success').click()

        self.driver.find_element(By.ID, 'country').send_keys('it')

        wait = WebDriverWait(self.driver, 12)
        wait.until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, 'Italy')))
        self.driver.find_element(By.LINK_TEXT, 'Italy').click()
        self.driver.find_element(
            By.XPATH, '//div[@class="checkbox checkbox-primary"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        success_message = self.driver.find_element(
            By.CLASS_NAME, 'alert-success').text

        assert 'Success! Thank you!' in success_message
        print('Success')
