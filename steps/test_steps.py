from behave import *
from page.login_page import LoginPage

@given('I open the login page')
def step_impl(context):
    context.login_page = LoginPage()
    context.login_page.open()

@when('I enter username "{user}"')
def step_impl(context, user):
    context.login_page.enter_username(user)

@when('I enter password "{pwd}"')
def step_impl(context, pwd):
    context.login_page.enter_password(pwd)

@when('I click login button')
def step_impl(context):
    context.login_page.click_login()

@then('I should see the home page')
def step_impl(context):
    assert context.login_page.on_home_page()