import time
import pytest
import pytest_bdd
from pytest_bdd import parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenario, given, then, when

@pytest.fixture

def browser():

    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@scenario('features/landing_page.feature', 'Go to the landing page')
def test_landing_page():
    pass

@given('I am on the landing page')
def open_landing_page(browser):
    browser.get('https://demoqa.com/')
    browser.maximize_window()

@then('the url should be true')
def verify_url(browser):
    assert browser.current_url == 'https://demoqa.com/'