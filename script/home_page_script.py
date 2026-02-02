import json
from core_framework.base_page import BasePage

class HomePageScript(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        with open("pages/home_page.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def go_to_home_page_by_url(self):
        self.driver.get("https://m.twitch.tv/")

    def close_popup_and_click_search(self):
        self.click_element("close_button")
        self.click_element("search_button")

