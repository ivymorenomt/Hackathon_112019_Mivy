from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Resources.Locators import Locators
from Data.Testdata import TestData
from Resources.Basepage import BasePage


class FlashSale(BasePage):

    def __init__(self, driver) :
        super().__init__(driver)
        self.driver.get(TestData.FLASH_SALE_URL)

    def load_page(self) :
        try:
         imagetest = self.driver.find_element(By.XPATH, '//*[@id="flashSale"]')
         findImage = imagetest.find_element(By.CSS_SELECTOR, '#flashSale > img')
         self.is_visible(findImage)
        except NoSuchElementException as elementexception:
            print('The element is not found', elementexception)