from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.need_review
@pytest.mark.parametrize('link', [
    pytest.param(
        f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{n}",
        marks=pytest.mark.xfail if n == 7 else []
    )
    for n in range(10)
])
def test_guest_can_add_product_to_basket(link, browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    print(f"Processing link: {link}")
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.click_on_add_to_cart()
    page.solve_quiz_and_get_code()
    page.book_name_presence_after_adding_book()
    page.book_price_presence_after_adding_book()


@pytest.mark.xfail(reason="This test should fail")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.click_on_add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="This test should fail")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.click_on_add_to_cart()
    page.solve_quiz_and_get_code()
    page.is_disappeared_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    bascket_page = BasketPage(browser, browser.current_url)
    bascket_page.basket_is_empty()
    bascket_page.empty_basket_message_present()


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org", "strong_password")
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.click_on_add_to_cart()
        page.solve_quiz_and_get_code()
        page.book_name_presence_after_adding_book()
        page.book_price_presence_after_adding_book()


    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()





