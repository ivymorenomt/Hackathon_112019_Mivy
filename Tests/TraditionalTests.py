import unittest
from selenium import webdriver

from Resources.PageObjects.Loginpage import HomePage
from Resources.PageObjects.UserLogsIn import UserLogin
from Resources.PageObjects.FinancialOverview import FinancialOverview
from Resources.PageObjects.FlashSale import FlashSale
from Resources.PageObjects.CanvasChart import CanvasChartPage
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

class Test_03_Table_Sort(Test_LoginPage_UI_Elements_Base):
	def setUp(self):
		super().setUp()

	def test_031_sort_and_validate_values(self):
		self.homePage = HomePage(self.driver)
		self.login = UserLogin(self.driver)
		self.login.login_username_password()
		self.financial = FinancialOverview(self.driver)
		self.financial.sort_table_values_and_match_values()

class Test_04_Canvas_Chart(Test_LoginPage_UI_Elements_Base):
	def setUp(self):
		super().setUp()

	def test_041_canvas_chart_test(self):
		self.homepage = HomePage(self.driver)
		self.login = UserLogin(self.driver)
		self.login.login_username_password()
		self.chart = CanvasChartPage(self.driver)
		self.chart.values_validate()

class Test_05_Dynamic_Content(Test_LoginPage_UI_Elements_Base):
	def setUp(self):
		super().setUp()

	def test_051_validate(self):
		self.sale = FlashSale(self.driver)
		self.sale.load_page()