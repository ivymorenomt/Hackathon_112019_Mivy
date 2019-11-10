import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from Resources.Locators import Locators
from Data.Testdata import TestData


class BasePage() :
    """This class is the parent class for all the pages in our application."""
    """It contains all common elements and functionalities available to all pages."""

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver) :
        self.driver = driver

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator) :
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    # this function asserts comparison of a web element's text with passed in text.
    def assert_text(self, by_locator, element_text) :
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert (web_element.text == element_text), 'Incorrect Text is displayed'

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text) :
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator) :
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator) :
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def assert_placeholder_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert (web_element.get_attribute('placeholder') == element_text), 'Incorrect placeholder text is displayed'
    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator) :
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()


class HomePage(BasePage) :

    def __init__(self, driver) :
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def verify_labels_present(self) :
        self.assert_text(Locators.LBLLOGIN, TestData.HEADERLABEL)
        self.assert_text(Locators.LBLUSERNAME, TestData.ULABEL)
        self.assert_text(Locators.LBLPASSWORD, TestData.PWDLABEL)
        self.assert_text(Locators.BTNLOGIN, TestData.LBLLOGIN)
        self.assert_text(Locators.LBLREMEMBER, TestData.LBLCHKBOX)
        self.assert_placeholder_text(Locators.TXTUSERNAME, TestData.TXTUSER)
        self.assert_placeholder_text(Locators.TXTPASSWORD, TestData.TXTPWD)

    def verify_icons_present(self) :
        self.is_visible(Locators.ICNUSER)
        self.is_visible(Locators.ICNPWD)
        self.is_visible(Locators.IMGTWITTER)
        self.is_visible(Locators.IMGLINKEDIN)
        self.is_visible(Locators.IMGFACEBOOK)


class UserLogin(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def login_no_credentials_entered(self):
        self.click(Locators.BTNLOGIN)
        self.assert_text(Locators.ALERT, TestData.CREDENTIALS_ALERT)

    def enter_password_only(self):
        self.driver.find_element(*Locators.TXTPASSWORD).clear()
        self.driver.find_element(*Locators.TXTUSERNAME).clear()
        self.enter_text(Locators.TXTPASSWORD, TestData.PASSWORD)
        self.click(Locators.BTNLOGIN)
        self.assert_text(Locators.ALERT, TestData.PASSWORD_ALERT)

    def enter_username_only(self):
        self.driver.find_element(*Locators.TXTUSERNAME).clear()
        self.driver.find_element(*Locators.TXTPASSWORD).clear()
        self.enter_text(Locators.TXTUSERNAME, TestData.USERNAME)
        self.click(Locators.BTNLOGIN)
        self.assert_text(Locators.ALERT, TestData.USERNAME_ALERT)

    def login_username_password(self):
        self.driver.find_element(*Locators.TXTUSERNAME).clear()
        self.driver.find_element(*Locators.TXTPASSWORD).clear()
        self.enter_text(Locators.TXTUSERNAME, TestData.USERNAME)
        self.enter_text(Locators.TXTPASSWORD, TestData.PASSWORD)
        self.click(Locators.BTNLOGIN)

    def login_remember_user(self):
        self.driver.find_element(*Locators.TXTUSERNAME).clear()
        self.driver.find_element(*Locators.TXTPASSWORD).clear()
        self.enter_text(Locators.TXTUSERNAME, TestData.USERNAME)
        self.enter_text(Locators.TXTPASSWORD, TestData.PASSWORD)
        self.click(Locators.CHKREMEMBER)
        self.click(Locators.BTNLOGIN)

    def verify_user_is_remembered(self):
        self.is_enabled(Locators.CHKREMEMBER)

        # REMARK
        # Unable to extract text entered by user in the Username field.
        # Unable to verify if the text matches with the test data that user provided upon remembering username


# class CartPage(BasePage) :
# 	"""Cart Page on Amazon India"""
#
# 	def __init__(self, driver) :
# 		super().__init__(driver)
#
# 	def delete_item(self) :
# 		cartCount = int(self.driver.find_element(*Locators.CART_COUNT).text)
# 		# print ("Cart Count is"+ str(cartCount))
# 		if (cartCount < 1) :
# 			print("Cart is empty")
# 			exit()
# 		if (self.driver.title.startswith("Amazon.in Shopping Cart")) :
# 			# to delete an item from the Cart
# 			self.click(Locators.DELETE_ITEM_LINK)
# 			time.sleep(2)
#
# 	def click_proceed_to_checkout_button(self) :
# 		self.click(Locators.PROCEED_TO_CHECKOUT_BUTTON)

