from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" This is the parent class for all page classes
   It contains all generic methods """

class BaseClass:

    def __init__(self, driver):
        self.driver = driver

    def explicit_wait(self, time = 10):
        return WebDriverWait(self.driver, time)

    def do_click(self, by_locator, time):
        self.explicit_wait(time).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_text(self, by_locator, text, time):
        self.explicit_wait(time).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator, time):
        element = self.explicit_wait(time).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_is_visible(self, by_locator, time):
        element = self.explicit_wait(time).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title, time):
        self.explicit_wait(time).until(EC.title_is(title))
        return self.driver.title
