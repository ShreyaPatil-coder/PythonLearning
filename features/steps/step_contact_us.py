import time

from behave import *
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

@given('launch the contactus browser')
def step_impl(context):
    context.driver = webdriver.Chrome(
        ChromeDriverManager().install())  # Optional argument, if not specified will search path.
    context.driver.get('http://www.google.com/')


@when('open the php contactus homepage')
def step_impl(context):
    context.driver.get('http://automationpractice.com/index.php')
    time.sleep(5)


@when('click on the contact us button')
def step_impl(context):
    contactus = context.driver.find_element_by_xpath('//*[@title="Contact Us"]')
    contactus.click()
    time.sleep(5)


@when('enter all the mandatory fields')
def step_impl(context):
    emailaddress = context.driver.find_element_by_id("email")
    emailaddress.send_keys('shreyapatil@gmail.com')
    orderreference = context.driver.find_element_by_name('id_order')
    orderreference.send_keys('234353')
    message = context.driver.find_element_by_id('message')
    message.send_keys('welcome')

    subjectheading = context.driver.find_element_by_xpath(
        "//select[@name='id_contact']/option[text()='Customer service']")
    subjectheading.click()


time.sleep(5)


@when('click on the submit')
def step_impl(context):
    send = context.driver.find_element_by_id('submitMessage')
    send.click()
    time.sleep(5)


@then('submitted successfully')
def step_impl(context):
    message = context.driver.find_element_by_class_name("alert-success")
    success_message = message.text
    assert success_message == "Your message has been successfully sent to our team."


@then('close the contactus browser')
def step_impl(context):
    context.driver.quit()
