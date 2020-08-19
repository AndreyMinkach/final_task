import pytest

from pages.locators import ProductPageLocators
from pages.product_page import ProductPage


linkk = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_empty_basket()
    page.should_be_basket_empty_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, linkk)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, linkk)
        product_page.open()
        product_page.should_not_be_success_message()
        product_page.is_not_element_present(*ProductPageLocators.ALERT_ADDED_TO_CART)

    def test_user_can_add_product_to_basket(self, browser):
        link = linkk
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_cart()
        product_page.should_be_present_in_cart()
        product_page.should_check_overall_cost()
