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
@scenario('features/web_table.feature', 'delete the first two lines and modify the salary of the remaining one')
def web_table():
    pass

@given('I go to the web table page')
def go_to_url(browser):
    browser.get('https://demoqa.com/webtables')
    browser.maximize_window()

@given('I delete the first two lines')
def delete_line(browser):
    time.sleep(1)
    browser.find_element(By.ID, "delete-record-1").click()
    browser.find_element(By.ID, "delete-record-2").click()



@given('I modify the salary of the remaining one')
def edit_line(browser):
    browser.find_element(By.ID, "edit-record-3").click()

    browser.find_element(By.ID, "salary").clear()

    browser.find_element(By.ID, "salary").send_keys("100000")
  
    browser.find_element(By.ID, "submit").click()
    time.sleep(1)

@then('I should see the salary modified')
def verify_edit(browser):
    assert browser.find_element(By.CSS_SELECTOR, ".rt-tr-group:nth-child(1) .rt-td:nth-child(5)").text == "100000"
    time.sleep(1)








