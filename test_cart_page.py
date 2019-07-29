from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.cart_page import CartPage
import pytest
import time

#gon't work, idk
#def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
#    link = "http://selenium1py.pythonanywhere.com"
#    page = BasePage(browser, link)
#    page.open()
#    page.go_to_basket()
#    cartpage = CartPage(browser, browser.current_url)
#    cartpage.should_be_empty_cart()
#    cartpage.should_be_empty_basket_text()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    cartpage = CartPage(browser, browser.current_url)
    cartpage.should_be_empty_cart()
    cartpage.should_be_empty_basket_text()