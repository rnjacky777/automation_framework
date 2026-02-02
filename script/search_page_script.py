import json
from core_framework.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        with open("search_page.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def perform_search(self, keyword):
        self.click_element("input_button")
        self.send_key('input_button', keyword)
        self.click_element('title1_button')

    def verify_results_and_playback(self, search_keyword):
        self.wait_element('streamer_button')
        self.scroll_page(500)
        self.wait_element('last_video')
        self.scroll_page(-500)
        self.click_element('streamer_button')
        self.wait_video_playing()
        self.element_screenshot(f"screenshot_{search_keyword}.png")