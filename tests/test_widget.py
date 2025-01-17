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
@scenario('features/widget.feature', 'Verify that the button Start finishes at 100%')
def test_presence_of_input_field():
    pass

@given('I am on the progress barre page')
def open_landing_page(browser):
    browser.get('https://demoqa.com/progress-bar')
    browser.maximize_window()

@when('I click on Start button')
def start_botton(browser):
    browser.find_element(By.XPATH, "//button[@id='startStopButton']").click()

@then('I verify that the button Start finishes at 100%')
def start_finish(browser):
    WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.XPATH, "//div[@class='progress-bar bg-success']"), "100%")
    )
    assert browser.find_element(By.XPATH, "//div[@class='progress-bar bg-success']").text == "100%"


@scenario('features/widget.feature', 'click on the sub sub item 2')
def sub_sub_item_2():
    pass

@given('I am on the widget menu page')
def go_to_menu_page(browser):
    browser.get('https://demoqa.com/menu')
    browser.maximize_window()

@when('I click on Main Item 2')
def click_main_item_2(browser):
    time.sleep(1)
    browser.find_element(By.XPATH, "//a[.='Main Item 2']").click()
    time.sleep(1)


@when('I click on Sub Sub List')
def click_su_sub_list(browser):
    sub_sub_list = browser.find_element(By.XPATH, "//a[.='SUB SUB LIST »']")
    webdriver.ActionChains(browser).move_to_element(sub_sub_list).perform()
    sub_sub_list.click()
    time.sleep(1)



@then('I can click the Sub Sub Item 2')
def verify(browser):
    assert browser.find_element(By.XPATH, "//a[.='Sub Sub Item 2']").is_displayed()
    browser.find_element(By.XPATH, "//a[.='Sub Sub Item 2']").click()









