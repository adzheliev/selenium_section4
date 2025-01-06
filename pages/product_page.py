from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_on_add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        link.click()

    def book_name_presence_after_adding_book(self):
        book_name_added = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_NAME).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_name_added == book_name

    def book_price_presence_after_adding_book(self):
        price_added = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_PRICE).text
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert price_added == price

