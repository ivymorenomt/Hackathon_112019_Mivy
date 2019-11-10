from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

	def __init__(self, driver):
		self.driver = driver

	def click(self, by_locator):
		WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

	def assert_text(self, by_locator, element_text):
		try :
			web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
			assert web_element.text == element_text
		except AssertionError as asserterror:
			print('Incorrect Text is displayed. ', asserterror)

	def assert_placeholder_text(self, by_locator, element_text):
		web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
		assert (web_element.get_attribute('placeholder') == element_text), 'Incorrect placeholder text is displayed'

	def get_column_data(self, by_locator):
		WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((by_locator)))

	def enter_text(self, by_locator, text):
		return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

	def is_enabled(self, by_locator):
		return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

	def is_visible(self, by_locator):
		try:
			element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
			return bool(element)
		except NoSuchElementException as elementexception:
			print('The element is not found', elementexception)

	def hover_to(self, by_locator):
		element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
		ActionChains(self.driver).move_to_element(element).perform()

	def assert_image(self, by_locator, image_locator):
		try:
			element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
			assert (element.get_attribute('src') == image_locator)
			print(element)
		except NoSuchElementException as elementexception:
			print('The element is not found', elementexception)
