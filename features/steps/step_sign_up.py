import time

from behave import *
from selenium import webdriver


@given('launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome(
        'C:\Program Files\chromedriver.exe')  # Optional argument, if not specified will search path.
    context.driver.get('http://www.google.com/')


@when('open the php homepage')
def step_impl(context):
    context.driver.get('http://automationpractice.com/index.php')
    time.sleep(5)


@when('click on the sign_in button')
def step_impl(context):
    signin = context.driver.find_element_by_xpath('//*[@title="Log in to your customer account"]')
    signin.click()
    time.sleep(1)


@when('enter email id and password and login')
def step_impl(context):
    emailid = context.driver.find_element_by_id('email')
    emailid.send_keys("shreyapatil1@gmail.com")
    password = context.driver.find_element_by_id('passwd')
    password.send_keys('shre#1234')
    time.sleep(5)
    signin1 = context.driver.find_element_by_id('SubmitLogin')
    signin1.click()
    time.sleep(5)


@then('verify the user is able to sign_in')
def step_impl(context):
    error_message = context.driver.find_element_by_class_name("alert-danger")
    message = error_message.text
    print("******%s*****" % message)
    assert message == "There is 1 error\nAuthentication failed."


@then('close the sign_in page')
def step_impl(context):
    context.driver.quit()
