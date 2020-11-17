import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

@given(u'Open the browser')
def step_impl(context):
    options = Options()
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    # Optional argument, if not specified will search path. # Optional argument, if not specified will search path.


@when(u'Open the google homepage which has search box')
def step_impl(context):
    context.driver.get('http://www.google.com/')


@then(u'Search for keyword \'Sample\' and verify the title of the browser.')
def step_impl(context):
    time.sleep(1)  # Let the user actually see something!
    search_box = context.driver.find_element_by_name('q')
    search_box.send_keys('Sample')
    search_box.submit()
    title = context.driver.title
    assert title == "Sample - Sök på Google"
    time.sleep(1)


@then(u'close the browser')
def step_impl(context):
    context.driver.quit()
