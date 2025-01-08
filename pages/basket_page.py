from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"
    

    def empty_basket_message_present(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE)
        assert 'Your basket is empty' in message.text