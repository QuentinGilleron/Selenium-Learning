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

# Aller sur demoqa.com
@scenario('features/alert_windows.feature', 'open and close new tab')
def test_presence_of_input_field():
    pass

@given('I go to the alert windows page')
def opent_browser_windows(browser):
    browser.get('https://demoqa.com/browser-windows')
    browser.maximize_window()

@when('I click on the button new tab')
def click_on_button(browser):
    browser.find_element(By.ID, 'tabButton').click()


@when('I see a new tab')
def verify_url(browser):
    # https://demoqa.com/sample
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)
    assert browser.current_url == "https://demoqa.com/sample"


@then('I close the new tab')
def step_then(browser):
    browser.close()

    original_tab = browser.window_handles[0]
    browser.switch_to.window(original_tab)
    assert browser.current_url == "https://demoqa.com/browser-windows"
