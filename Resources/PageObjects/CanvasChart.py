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