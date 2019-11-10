import time

from Resources.Locators import Locators
from Data.Testdata import TestData
from Resources.Basepage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver

class FinancialOverview(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def sort_table_values_and_match_values(self):
            #gather all values in a list and verify values first
        table_values = []
        for r in range(1, 7) :
            unsortedrows = (
                self.driver.find_element(By.XPATH, f'//*[@id="transactionsTable"]/tbody/tr[{r}]/td[5]/span'))
            table_values.append(unsortedrows.text)
        assert table_values == TestData.UNSORTED_VALUES
        self.click(Locators.AMOUNT)

        #gather all values again and verify sorted list
        sortedtable_values = []
        for r in range(1, 7) :
            sortedrows = (
                self.driver.find_element(By.XPATH, f'//*[@id="transactionsTable"]/tbody/tr[{r}]/td[5]/span'))
            sortedtable_values.append(sortedrows.text)
        try:
            assert (sortedtable_values == TestData.SORTED_VALUES), f'Sorted values do not match {sortedtable_values}'
        except AssertionError as asserterror :
             print(f'Sorted values do not match {sortedtable_values}', asserterror)


