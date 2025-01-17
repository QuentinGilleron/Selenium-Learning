import time
import pytest
import pytest_bdd
from pytest_bdd import parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenario, given, then, when
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture

def browser():

    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Aller sur demoqa.com
@scenario('features/select_menu.feature', 'Select values')
def test_select_values():
    pass

@given('I am on the select menu page')
def menu_page(browser):
    browser.get('https://demoqa.com/select-menu')
    browser.maximize_window()

@when('I select Another root option')
def select_root(browser):
    browser.execute_script("window.scrollTo(0, 300)")

    browser.find_element(By.ID, 'withOptGroup').click()
    browser.find_element(By.ID, 'react-select-2-option-3').click()

    root = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, 'withOptGroup'),
                "Another root option"
            )
        )
    assert root

@when('I select Select one other')
def select_other(browser):
    browser.find_element(By.ID, 'selectOne').click()
    browser.find_element(By.ID, 'react-select-3-option-0-5').click()

    other = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, 'selectOne'),
                "Other"
            )
        )
    assert other

@when('I select Old style select menu aqua')
def select_aqua(browser):

    browser.find_element(By.ID, 'oldSelectMenu').click()
    browser.find_element(By.XPATH, "//option[.='Aqua']").click()
    aqua = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, 'oldSelectMenu'),
                "Aqua"
            )
        )
    assert aqua
    
@then('I select Multi select drop down red and black')
def red_and_black_drop_down(browser):
    browser.find_element(By.XPATH, '//*[@id="selectMenuContainer"]/div[7]/div/div/div').click()
    browser.find_element(By.ID, "react-select-4-option-3").click()
    browser.find_element(By.ID, "react-select-4-option-2").click()
    browser.find_element(By.XPATH, '//*[@id="selectMenuContainer"]/div[7]/div/div/div').click()

    red_text = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '.css-1pahdxg-control > .css-1hwfws3 > div:nth-of-type(1) .css-12jo7m5'),
                "Red"
            )
        )
    
    black_text = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '.css-1pahdxg-control > .css-1hwfws3 > div:nth-of-type(2) .css-12jo7m5'),
                "Black"
            )
        )
        
    assert red_text
    assert black_text








