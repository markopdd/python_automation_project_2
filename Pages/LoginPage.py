from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BaseClass import BaseClass


class LoginPage(BaseClass):

     """By locators"""
     SIGN_UP_LINK = (By.CLASS_NAME, "signup_link signup-button")

     EMAIL = (By.XPATH, "//input[@name='determine_email']")
     PASSWORD = (By.ID, "signup_password")

     NEXT_BUTTON = (By.XPATH, "//span[@class='signup_determine_btn active']")
     SIGN_UP_WITH_PASSWORD = (By.XPATH, "//div[@id='signup_magiclink']//a[@class='forgot_password_link'][contains(text(),'Войти с паролем')]")
     LOGIN_BUTTON = (By.XPATH, "//span[@class='signup_login_btn active']")


     """Constructor of the Page Claass"""
     def __init__(self, driver):
          super().__init__(driver)
          self.driver.get(TestData.BASE_URL)

     """Page actions"""
     def get_login_page_title(self, title):
          return self.get_title(title)

     def is_signup_link_exist(self):
          return self.get_is_visible(self.SIGN_UP_LINK)

     def do_login(self, username, password):
          self.do_send_keys(self.EMAIL, username)
          self.do_click(self.NEXT_BUTTON)
          self.do_click(self.SIGN_UP_WITH_PASSWORD)
          self.do_send_keys(self.PASSWORD, password)
          # self.do_click(self.NEXT_BUTTON)
          self.do_click(self.LOGIN_BUTTON)
