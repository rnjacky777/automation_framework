import pytest
from unittest import TestCase
import core_framework.core_framework as core_framework
from validator.home_page_validator import HomePageValidator
from page.home_page import HomePage
from script.home_page_script import HomePageScript
from script.cart_page import CartPageScript

@pytest.mark.usefixture("init_driver")
class TestFirst(TestCase):
    def setUp(self):
        self.home_page = HomePage()
        self.home_page_script = HomePageScript()
        self.cart_page_script = CartPageScript()
        self.home_page_validator = HomePageValidator()

    def tearDown(self):
        # core_framework.CoreDriver.driver.quit()
        pass

    # @pytest.mark.usefixture("init_driver")
    def test_first_testcase_1(self):
        self.home_page_script.go_to_homepage()
        # self.home_page_script.load_cookie()
        # self.home_page_script.page_refresh()
        self.home_page_script.wait_page_loading()
        self.home_page_script.close_pop_up_banner()
        self.home_page_validator.check_search_button_exist()
        # self.home_page.cart_icon().click()
        # self.cart_page_script.select_all_checkbox().click()
    def test_first_testcase_2(self):
        self.home_page_script.go_to_homepage()
        # self.home_page_script.load_cookie()
        # self.home_page_script.page_refresh()
        self.home_page_script.wait_page_loading()
        self.home_page_script.close_pop_up_banner()
        self.home_page_validator.check_search_button_exist()
