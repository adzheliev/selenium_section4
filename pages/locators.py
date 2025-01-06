from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    BOOK_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    BOOK_PRICE = (By.XPATH, '//p[@class="price_color"]')
    ADDED_BOOK_NAME = (By.XPATH, '//div[@id="messages"]//div[@class="alert alert-safe alert-noicon alert-success  fade in"][1]//strong')
    ADDED_BOOK_PRICE = (By.XPATH, '//div[@id="messages"]//div[@class="alert alert-safe alert-noicon alert-info  fade in"]//strong')
