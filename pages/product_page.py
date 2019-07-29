from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
import math
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_item_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADDTOBASKET)
        add_to_basket_button.click()
		
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
	
    def should_be_item_name(self):
        name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        name_inner = self.browser.find_element(*ProductPageLocators.ITEM_NAME_INNER).text
        assert name == name_inner, "Needed name = {}, get = {}".format(name, name_inner)

    def should_be_item_price(self):
        price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        price_inner = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_INNER).text
        assert price == price_inner, "Needed price = {}, get = {}".format(price, price_inner)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

