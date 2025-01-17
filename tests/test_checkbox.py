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


@scenario('features/checkbox.feature', 'Select all the element except Office and Excel file.doc')
def test_checkbox():
    pass

@given('I go to the check box page')
def check_box_page(browser):
    browser.get('https://demoqa.com/checkbox')
    browser.maximize_window()

@when('I select all the element except Office and Excel file.doc')
def check_some_box(browser):
    browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/button').click()
    browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/span/button').click()
    browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/span/button').click()
    browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/button').click()
    browser.find_element(By.XPATH,'//div[@id="tree-node"]//span[@class="rct-text"]//span[.="Desktop"]').click()
    # scroll down
    browser.execute_script("window.scrollTo(0, 300)")
    browser.find_element(By.XPATH, "//div[@id='tree-node']//span[@class='rct-text']//span[.='WorkSpace']").click()
    browser.find_element(By.XPATH, "//div[@id='tree-node']//span[@class='rct-text']//span[.='Word File.doc']").click()

@then('I should see the element selected')
def verify_if_checked(browser):
    expected_values = [
        "desktop",
        "notes",
        "commands",
        "workspace",
        "react",
        "angular",
        "veu",
        "wordFile",
    ]
    for i, val in enumerate(expected_values, start=2):
        assert browser.find_element(By.XPATH, f'//*[@id="result"]/span[{i}]').text == val

















