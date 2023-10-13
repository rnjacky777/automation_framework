from page.home_page import HomePage


class HomePageValidator(HomePage):

    def __init__(self) -> None:
        super().__init__()

    def check_search_button_exist(self):
        assert self.search_button() is not None
    
    def check_cart_icon_exist(self):
        assert self.cart_icon() is not None

