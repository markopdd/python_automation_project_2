import pytest
from Tests.test_base import BaseTest

from Config.config import TestData
from Pages.LoginPage import LoginPage

class Test_LoginPage(BaseTest):

    # def test_signup_link_visible(self):
    #     self.login_page = LoginPage(self.driver)
    #     flag = self.login_page.is_signup_link_exist()
    #     assert flag

    def test_login_page_title(self):
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.EMAIL, TestData.PASSWORD)