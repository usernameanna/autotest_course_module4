from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTNBASKET = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")

#class MainPageLocators(object):

    
	
class LoginPageLocators(object):
    LOGIN_URL = (By.CSS_SELECTOR, "#login_url")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
    ADDTOBASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main >p.price_color")
    ITEM_NAME_INNER = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    ITEM_PRICE_INNER = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")

class CartPageLocators(object):
    BUSKETITEMS = (By.CSS_SELECTOR, "#basket_formset > div")
    EMPTYBASKET = (By.CSS_SELECTOR, "#content_inner > p")