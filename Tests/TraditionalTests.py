import unittest
from selenium import webdriver

from Resources.PageObjects.Loginpage import HomePage
from Resources.PageObjects.UserLogsIn import UserLogin
from Data.Testdata import TestData

class Test_LoginPage_UI_Elements_Base(unittest.TestCase):

	def setUp(self):
		chrome_options = webdriver.ChromeOptions()
		self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH, options=chrome_options)
		self.driver.maximize_window()

	def tearDown(self):
		self.driver.close()
		self.driver.quit()

class Test_01_LoginPage_UI_Elements(Test_LoginPage_UI_Elements_Base):
	def setUp(self):
		super().setUp()

	def test_001_login_page_elements(self):
		self.homePage = HomePage(self.driver)
		self.homePage.verify_labels_present()
		self.homePage.verify_icons_present()

class Test_02_Data_Driven(Test_LoginPage_UI_Elements_Base):
	def setUp(self):
		super().setUp()

	def test_021_login_invalid_credentials(self):
		self.homePage = HomePage(self.driver)
		self.login = UserLogin(self.driver)
		self.login.login_no_credentials_entered()
		self.login.enter_password_only()
		self.login.enter_username_only()

	def test_022_login_valid_credentials(self):
		self.homePage = HomePage(self.driver)
		self.login = UserLogin(self.driver)
		self.login.login_username_password()

	def test_023_login_verify_user_remembered(self):
		self.homePage = HomePage(self.driver)
		self.login = UserLogin(self.driver)
		self.login.login_remember_user()
		self.driver.back()
		self.login.verify_user_is_remembered()