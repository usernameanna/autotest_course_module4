from .base_page import BasePage
from .locators import CartPageLocators
from selenium.common.exceptions import NoSuchElementException

class CartPage(BasePage):

    def should_be_empty_cart(self):
       assert self.is_not_element_present(*CartPageLocators.BUSKETITEMS), "Have items in cart"

    def should_be_empty_basket_text(self):
        assert self.browser.find_element(*CartPageLocators.EMPTYBASKET).text
        text = self.browser.find_element(*CartPageLocators.EMPTYBASKET).text
        assert text,"Cart is not empty, have items"
