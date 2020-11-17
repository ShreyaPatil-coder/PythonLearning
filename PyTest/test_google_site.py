import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Test_Google():

    @pytest.fixture()
    def test_setup(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = SeleneDriver.wrap(webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options))
        yield
        self.driver.quit()

    def test_search_case(self, test_setup):
        self.driver.get('http://www.google.com/')
        time.sleep(5)  # Let the user actually see something!
        search_box = self.driver.find_element_by_name('q')
        search_box.send_keys('ChromeDriver')
        search_box.submit()
        title = self.driver.title
        assert title == "ChromeDriver - Sök på Google"
        time.sleep(5)
