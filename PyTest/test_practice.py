import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager


class Test_abc():
    @pytest.fixture()
    def test_setup(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)


        self.driver.get('http://automationpractice.com/index.php')

        yield
        self.driver.quit()

    def test_practice(self, test_setup):
        contactus = self.driver.find_element_by_xpath('//*[@title="Contact Us"]')
        contactus.click()
        time.sleep(1)
        emailaddress = self.driver.find_element_by_id("email")
        emailaddress.send_keys('shreyapatil@gmail.com')
        orderreference = self.driver.find_element_by_name('id_order')
        orderreference.send_keys('234353')
        message = self.driver.find_element_by_id('message')
        message.send_keys('welcome')

        subjectheading = self.driver.find_element_by_xpath(
            "//select[@name='id_contact']/option[text()='Customer service']")
        subjectheading.click()
        time.sleep(1)
        send = self.driver.find_element_by_id('submitMessage')
        send.click()
        time.sleep(1)
        success_message = self.driver.find_element_by_class_name("alert-success")
        value = success_message.text
        assert value == "Your message has been successfully sent to our team."
