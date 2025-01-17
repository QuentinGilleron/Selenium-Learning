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
@scenario('features/search_book.feature', 'Search for a book')
def serch_book():
    pass

@given('I am on the book page')
def book_page(browser):
    browser.get('https://demoqa.com/books')
    browser.maximize_window()

@when('I search for Marijn Haverbeke')
def search(browser):
    search_input = browser.find_element(By.XPATH, "//input[@id='searchBox']")
    search_input.send_keys('Marijn Haverbeke')
    search_input.send_keys(Keys.RETURN)


@then('I verify that the search result is correct')
def verify_result(browser):
    search_result = browser.find_element(By.XPATH, "//div[.='Marijn Haverbeke']")
    assert search_result.text == 'Marijn Haverbeke'




