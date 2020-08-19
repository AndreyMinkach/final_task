import time

import pytest

from pages.locators import ProductPageLocators
from pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
links = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
linkk = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, linkk)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, linkk)
    product_page.open()
    product_page.should_not_be_success_message()
    product_page.is_not_element_present(*ProductPageLocators.ALERT_ADDED_TO_CART)


def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, linkk)
    product_page.open()
    product_page.add_to_cart()
    product_page.is_disappeared(*ProductPageLocators.ALERT_ADDED_TO_CART)


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(2)
    page.go_to_basket_page()
    page.should_be_empty_basket()
    page.should_be_basket_empty_message()


@pytest.mark.xfail
@pytest.mark.parametrize("product", links)
def test_guest_can_add_product_to_basket(browser, product: str) -> None:
    link = product
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()
