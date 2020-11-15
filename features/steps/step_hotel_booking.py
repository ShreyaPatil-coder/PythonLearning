import time

from behave import when, then, given
from selenium import webdriver


@given('Browser is launch')
def step_impl(context):
    context.driver = webdriver.Chrome(
        'C:\Program Files\chromedriver.exe')  # Optional argument, if not specified will search path.
    context.driver.get('http://www.google.com/')


@given('open the Php hotel homepage')
def step_impl(context):
    context.driver.get('http://phptravels.net')
    time.sleep(5)


@when('enter the destination')
def step_impl(context):
    destination = context.driver.find_element_by_css_selector("input[type='text']")
    destination.send_keys('Tria Hotel Istanbul Especial')
    time.sleep(2)
    hotel_name = context.driver.find_element_by_class_name("select2-match")
    hotel_name.click()


@when('select the check in date and check out date')
def step_impl(context):
    checkin = context.driver.find_element_by_id('checkin')
    checkin.clear()
    checkin.send_keys('20/09/2020')
    checkout = context.driver.find_element_by_id('checkout')
    checkout.clear()
    checkout.send_keys('2/10/2020')

    time.sleep(1)


@when('enter the adult number')
def step_impl(context):
    adult_minus = context.driver.find_elements_by_xpath(
        '//*[@id="hotels"]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[1]/div/div[2]/div/span/button[2]')[0]
    adult_minus.click()
    time.sleep(1)
    adult_plus = context.driver.find_elements_by_xpath(
        '//*[@id="hotels"]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[1]/div/div[2]/div/span/button[1]')[0]
    adult_plus.click()
    adult_plus.click()
    adult_plus.click()


@when(u'enter the children number')
def step_impl(context):
    children = context.driver.find_elements_by_xpath(
        '//*[@id="hotels"]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div[2]/div/span/button[2]')[0]
    children.click()
    children_add = context.driver.find_elements_by_xpath(
        '//*[@id="hotels"]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div[2]/div/span/button[1]')[0]
    children_add.click()
    children_add.click()
    time.sleep(1)


@when('click on the search button')
def step_impl(context):
    search = context.driver.find_elements_by_xpath('//*[@id="hotels"]/div/div/form/div/div/div[4]/button')[0]
    # search = context.driver.find_element_by_id('Search')
    # search = context.driver.find_element_by_class_name('btn btn-primary btn-block')
    search.submit()
    time.sleep(9)


@then('hotel should get search')
def step_impl(context):
    time.sleep(1)


##Scenario 2
@given('Hotel should get searched')
def step_impl(context):
    context.driver = webdriver.Chrome(
        'C:\Program Files\chromedriver.exe')
    time.sleep(1)


@when('click on the first searched hotel details button')
def step_impl(context):
    details = context.driver.find_elements_by_xpath(
        '/html/body/div[1]/div[1]/div[1]/section/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[3]/div/div[2]/a')
    # details = context.driver.find_element_by_class_name('btn btn-primary btn-sm btn-wide')
    details.submit()
    time.sleep(1)


@then('Details should get displayed')
def step_impl(context):
    time.sleep(1)
