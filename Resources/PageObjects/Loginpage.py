from Resources.Locators import Locators
from Data.Testdata import TestData
from Resources.Basepage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def verify_labels_present(self):
        self.driver.find_element(*Locators.LBLLOGIN)
        self.assert_text(Locators.LBLLOGIN, TestData.HEADERLABEL)
        self.assert_text(Locators.LBLUSERNAME, TestData.ULABEL)
        self.assert_text(Locators.LBLPASSWORD, TestData.PWDLABEL)
        self.assert_text(Locators.BTNLOGIN, TestData.LBLLOGIN)
        self.assert_text(Locators.LBLREMEMBER, TestData.LBLCHKBOX)
        self.assert_placeholder_text(Locators.TXTUSERNAME, TestData.TXTUSER)
        self.assert_placeholder_text(Locators.TXTPASSWORD, TestData.TXTPWD)

    def verify_icons_present(self):
        self.is_visible(Locators.ICNUSER)
        self.is_visible(Locators.ICNPWD)
        self.is_visible(Locators.IMGTWITTER)
        self.is_visible(Locators.IMGLINKEDIN)
        self.is_visible(Locators.IMGFACEBOOK)
