from Resources.Locators import Locators
from Data.Testdata import TestData
from Resources.Basepage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver

class CanvasChartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def values_validate(self):
        self.click(Locators.LNKCOMPARE)
        self.click(Locators.BTNSHOWDATA)
		# REMARK: Unable to continue testing. My plan is to extract values from the javascript itself.
		# size of the canvas does not change at all and I don't think it would be able to validate it properly.