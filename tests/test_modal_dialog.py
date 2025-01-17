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


@scenario('features/modal_dialog.feature', 'Verify text in large dialogue')
def test_modal_dialog():
    pass

@given('I go to the modal dialogs page')
def open_modal_dialog_page(browser):
    browser.get('https://demoqa.com/modal-dialogs')
    browser.maximize_window()

@when('I click on the large dialogue button')
def click_bouton(browser):
    assert browser.find_element(By.XPATH, '//*[@id="showLargeModal"]').is_displayed()
    browser.find_element(By.XPATH, '//*[@id="showLargeModal"]').click()

@then('I should see the text lorem ipsum 4 times')
def verify_text(browser):
    modal_body = browser.find_element(By.CSS_SELECTOR, ".modal-body")
    occurrences = modal_body.text.count("Lorem Ipsum")
    assert occurrences == 4, f"Expected 4 occurrences, but found {occurrences}."

