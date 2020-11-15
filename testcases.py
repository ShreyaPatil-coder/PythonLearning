import time

from selenium import webdriver


class Testcases:

    def __init__(self):
        self.driver = webdriver.Chrome(
            'C:\Program Files\chromedriver.exe')  # Optional argument, if not specified will search path.
        self.driver.get('http://www.google.com/')

    def scenario1(self):
        time.sleep(5)  # Let the user actually see something!
        search_box = self.driver.find_element_by_name('q')
        search_box.send_keys('ChromeDriver')
        search_box.submit()
        time.sleep(5)  # Let the user actually see some

        # thing!

    def scenario2(self):
        time.sleep(5)  # Let the user actually see something!
        search_box = self.driver.find_element_by_name('q')
        search_box.send_keys('shreya')
        search_box.submit()
        time.sleep(5)  # Let the user actually see some

    def scenario3(self):
        self.driver.get('http://automationpractice.com/index.php')
        time.sleep(5)
        search_box = self.driver.find_element_by_id("search_query_top")
        search_box.send_keys('alzer')
        submit_button = self.driver.find_element_by_name("submit_search")
        submit_button.submit()
        time.sleep(5)

    def scenario4(self):
        # // *[ @ id = "contact-link"] / a
        self.driver.get('http://automationpractice.com/index.php')
        time.sleep(5)
        signin = self.driver.find_element_by_xpath('//*[@title="Log in to your customer account"]')
        signin.click()
        time.sleep(5)
        emailid = self.driver.find_element_by_id('email')
        emailid.send_keys("shreyapatil1@gmail.com")
        password = self.driver.find_element_by_id('passwd')
        password.send_keys('shre#1234')
        time.sleep(5)
        signin1 = self.driver.find_element_by_id('SubmitLogin')
        signin1.click()
        time.sleep(5)
        error_message = self.driver.find_element_by_class_name("alert-danger")
        message = error_message.text
        print("***** %s" % message)

        # contactus = self.driver.find_element_by_xpath('//*[@title="Contact Us"]')
        # contactus.click()
        # time.sleep(5)
        # emailaddress = self.driver.find_element_by_id("email")
        # emailaddress.send_keys('shreyapatil@gmail.com')
        # orderreference = self.driver.find_element_by_name('id_order')
        # orderreference.send_keys('234353')
        # message = self.driver.find_element_by_id('message')
        # message.send_keys('welcome')
        #
        # subjectheading = self.driver.find_element_by_xpath(
        #     "//select[@name='id_contact']/option[text()='Customer service']")
        # subjectheading.click()
        # time.sleep(5)
        # send = self.driver.find_element_by_id('submitMessage')
        # send.click()
        # time.sleep(5)

    def stoptestcases(self):
        self.driver.quit()
