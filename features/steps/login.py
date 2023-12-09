from selenium import webdriver
from features.pages.Login_Page import LoginPage
from selenium.webdriver.chrome.options import Options
from behave import *


@given(u': User can load the demo website')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    driver = context.driver
    context.username = "Admin"
    context.password = "admin123"
    login_url = "https://opensource-demo.orangehrmlive.com/"
    driver.get(login_url)


@when(u': Enter Username')
def step_impl(context):
    driver = context.driver
    context.login = LoginPage(driver)
    context.login.enter_username(context.username)


@when(u': Enter Password')
def step_impl(context):
    driver = context.driver
    context.login = LoginPage(driver)
    context.login.enter_password(context.password)


@when(u': Click Login Button')
def step_impl(context):
    driver = context.driver
    context.login = LoginPage(driver)
    context.login.click_button()


@then(u': User should be logged in successfully')
def step_impl(context):
    driver = context.driver
    actual_title = driver.title
    expected_title = "OrangeHRM"
    assert actual_title == expected_title
