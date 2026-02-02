import pytest
import allure
from script.home_page_script import HomePageScript
from script.search_page_script import SearchPage

@pytest.mark.parametrize("search_term, url_term", [("StarCraft II", "StarCraft%20II")])
def test_twitch_ui_workflow(shared_driver, search_term, url_term):
    with allure.step('init class'):
        home_script = HomePageScript(shared_driver)
        search_script = SearchPage(shared_driver)

    home_script.go_to_home_page_by_url()
    home_script.close_popup_and_click_search()
    
    search_script.perform_search(search_term)
    search_script.wait_url_contains(url_term) 
    search_script.verify_results_and_playback(search_term)