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
         findImage = imagetest.find_element(By.XPATH, '//*[@id="flashSale"]/img')
         imagetest2 = self.driver.find_element(By.XPATH, '//*[@id="flashSale2"]')
         findImage2 = imagetest2.find_element(By.XPATH, '//*[@id="flashSale2"]/img')
         imgName = findImage.get_attribute('src')
         imgName2 = findImage2.get_attribute('src')
         assert imgName == TestData.SRCIMG1
         assert imgName2 == TestData.SRCIMG2
         print(imgName)
         print(imgName2)
        except NoSuchElementException as elementexception:
            print('The element is not found', elementexception)