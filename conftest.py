import pytest
from selenium import webdriver

@pytest.fixture(params=["Chrome"], scope='class')
def init_driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome()
    elif request.param == "Firefox":
        driver = webdriver.Firefox()

    request.cls.driver = driver
    yield
    driver.close()

