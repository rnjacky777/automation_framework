import core_framework
from script.home_page import HomePageScript
from script.cart_page import CartPageScript
import time
def test_first_testcase():
    core_framework.CoreDriver.driver= core_framework.init_driver()
    a = HomePageScript()
    b = CartPageScript()
    try:
        a.go_to_homepage()
        a.load_cookie()
        a.page_refresh()
        a.wait_page_loading()
        a.close_pop_up_banner()
        a.cart_icon().click()
        b.select_all_checkbox().click()
    except:
        core_framework.CoreDriver.driver.close()
        raise ValueError

    # time.sleep(5)
    
    # a.search_button().click()
    