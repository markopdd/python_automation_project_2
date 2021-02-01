from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BaseClass import BaseClass


class LoginPage(BaseClass):

     """By locators"""
     EMAIL = (By.XPATH, "//input[@id='username']")
     PASSWORD = (By.XPATH, "//input[@id='password']")
     SIGN_UP_CHECKBOX = (By.XPATH, "//span[@id='checkbox-content-4']")
     LOGIN_BUTTON = (By.XPATH, "//button[@id='loginBtn']")


     """Constructor of the Page Claass"""
     def __init__(self, driver):
          super().__init__(driver)
          self.driver.get(TestData.BASE_URL)

     """Page actions"""
     def get_login_page_title(self, title):
          return self.get_title(title)

     def is_signup_link_exist(self):
          return self.get_is_visible(self.SIGN_UP_CHECKBOX)

     def do_login(self, username, password):
          self.do_send_text(self.EMAIL, username)
          self.do_send_text(self.PASSWORD, password)
          self.do_click(self.LOGIN_BUTTON)
