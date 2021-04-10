#from django.test import TestCase
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(browser):
    browser.get("http://http://localhost:8000/auth/login/")
    src = browser.page_source
    assert 'PyBites Login' in src
    browser.find_element_by_name('username').send_keys('Robby')
    browser.find_element_by_name('password').send_keys('auth1234' + Keys.RETURN)
    src =browser.page_source
    assert 'Logout' in src
    assert 'Login' not in src

