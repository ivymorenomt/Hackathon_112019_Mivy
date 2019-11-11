from selenium import webdriver
from applitools.selenium import Eyes
from applitools.common.config import BatchInfo
from selenium.webdriver.common.by import By
from Data.Testdata import TestData

class ValidateLoginUIElements() :
    eyes = Eyes()

    # Initialize the eyes SDK and set your private API key.
    eyes.api_key = TestData.API_KEY

    try :

        # Open a Chrome browser.
        driver = webdriver.Chrome()

        eyes.open(driver, TestData.APP_NAME, "Validate Login UI Elements", TestData.VIEW_PORT)
        batch = BatchInfo('Login UI Test')
        driver.get(TestData.BASE_URL)
        eyes.check_window('Login UI Elements', 10)

        # End the test.
        eyes.close()

    finally :

        # Close the browser.
        driver.quit()

        # If the test was aborted before eyes.close was called, ends the test as aborted.
        eyes.abort()


class DataDriven() :
    eyes = Eyes()
    eyes.api_key = TestData.API_KEY

    try :
        driver = webdriver.Chrome()
        eyes.open(driver, TestData.APP_NAME, "Data Driven Test", TestData.VIEW_PORT)
        batch = BatchInfo('Data Driven Test')

        driver.get(TestData.BASE_URL)

        btnlogin = driver.find_element(By.XPATH, '//*[@id="log-in"]')
        btnlogin.click()
        eyes.check_window('Username and Password alert window check', 10)

        txtusername = driver.find_element(By.ID, 'username')
        txtpassword = driver.find_element(By.ID, 'password')
        chkremember = driver.find_element(By.CLASS_NAME, 'form-check-input')

        txtusername.click()
        txtusername.send_keys(TestData.USERNAME)
        btnlogin.click()
        eyes.check_window('Entered username only alert check', 10)
        txtusername.clear()
        txtpassword.send_keys(TestData.PASSWORD)
        btnlogin.click()
        eyes.check_window('Entered password only alert check', 10)
        txtusername.click()
        txtusername.send_keys(TestData.USERNAME)
        chkremember.click()
        btnlogin.click()
        eyes.check_window('Verify that the user has successfully logged in', 10)
        driver.back()
        eyes.check_window('Verify that the username is remembered and Remember Me checkbox is checked', 10)
        # End the test.
        eyes.close()

    finally :

        # Close the browser.
        driver.quit()
        # If the test was aborted before eyes.close was called, ends the test as aborted.
        eyes.abort()


class Table_Sort_Test :
    eyes = Eyes()
    eyes.api_key = TestData.API_KEY

    try :
        driver = webdriver.Chrome()
        eyes.open(driver, TestData.APP_NAME, "Table Sort", TestData.VIEW_PORT)
        batch = BatchInfo('Data Driven Test')
        driver.get(TestData.BASE_URL)

        btnlogin = driver.find_element(By.XPATH, '//*[@id="log-in"]')
        txtusername = driver.find_element(By.ID, 'username')
        txtpassword = driver.find_element(By.ID, 'password')

        txtusername.clear()
        txtusername.send_keys(TestData.USERNAME)
        txtpassword.clear()
        txtpassword.send_keys(TestData.PASSWORD)
        btnlogin.click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        eyes.check_window('Validate values before sorting Amount column', 10)
        amount = driver.find_element(By.ID, 'amount')
        amount.click()
        eyes.check_window('Validate amount column after sorting', 10)
        eyes.close()

    finally :
        driver.quit()
        eyes.abort()


class CanvasChart :
    eyes = Eyes()
    eyes.api_key = TestData.API_KEY

    try :
        driver = webdriver.Chrome()
        eyes.open(driver, TestData.APP_NAME, "Canvas Chart", TestData.VIEW_PORT)
        batch = BatchInfo('Canvas Chart Test')

        driver.get(TestData.BASE_URL)

        btnlogin = driver.find_element(By.XPATH, '//*[@id="log-in"]')
        txtusername = driver.find_element(By.ID, 'username')
        txtpassword = driver.find_element(By.ID, 'password')

        txtusername.clear()
        txtusername.send_keys(TestData.USERNAME)
        txtpassword.clear()
        txtpassword.send_keys(TestData.PASSWORD)
        btnlogin.click()
        compare_exp = driver.find_element(By.ID, 'showExpensesChart')
        compare_exp.click()
        eyes.check_window('Validate expenses between 2017 and 2018', 10)
        show_data = driver.find_element(By.ID, 'addDataset')
        show_data.click()
        eyes.check_window('Validate expenses between 2017, 2018 and 2019', 10)

        eyes.close()

    finally :
        driver.quit()
        eyes.abort()

class DynamicContent:
    eyes = Eyes()
    eyes.api_key = TestData.API_KEY

    try :
        driver = webdriver.Chrome()
        eyes.open(driver, TestData.APP_NAME, "Dynamic Content", TestData.VIEW_PORT)
        batch = BatchInfo('Dynamic Content')
        driver.get(TestData.FLASH_SALE_URL)
        eyes.check_window('Validate flash sale GIFs are displayed', 10)

        eyes.close()

    finally :

        # Close the browser.
        driver.quit()

        # If the test was aborted before eyes.close was called, ends the test as aborted.
        eyes.abort()