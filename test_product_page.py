from .pages.product_page import ProductPage
import pytest
from time import sleep


# @pytest.mark.parametrize('link', [
#     pytest.param(
#         f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{n}",
#         marks=pytest.mark.xfail if n == 7 else []
#     )
#     for n in range(10)
# ])
def test_guest_can_add_product_to_basket(browser):
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





