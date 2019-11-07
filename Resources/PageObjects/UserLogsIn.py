from Resources.Locators import Locators
from Data.Testdata import TestData
from Resources.Basepage import BasePage


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
        # Unable to extract text entered by user in the Username field.
        # Unable to verify if the text matches with the test data that user provided upon remembering username
