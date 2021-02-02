import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class ConfirmPage:

    EMAIL = (By.XPATH, "//input[@id='username']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    SIGN_UP_CHECKBOX = (By.XPATH, "//span[@id='checkbox-content-4']")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='loginBtn']")

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = self.driver.get("https://app.hubspot.com/login")
        self.time = time.sleep(10)

    def check_country(self):
        return self.driver.find_element(*ConfirmPage.EMAIL)

    def country_results(self):
        return self.driver.find_element(*ConfirmPage.PASSWORD)

    def checkbox_mark(self):
        return self.driver.find_element(*ConfirmPage.SIGN_UP_CHECKBOX)

    def purchase_button(self):
        return self.driver.find_element(*ConfirmPage.LOGIN_BUTTON)


test_1 = ConfirmPage().check_country().click()
ConfirmPage().country_results().click()
ConfirmPage().checkbox_mark().click()
ConfirmPage().purchase_button().click()
