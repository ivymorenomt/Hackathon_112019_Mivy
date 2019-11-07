from selenium.webdriver.common.by import By

class Locators():

#Locators for Login Page
	# labels in Login UI
	LBLLOGIN = (By.CLASS_NAME, 'auth-header')
	LBLUSERNAME = (By.XPATH, '//*[contains(text(), "Username")]')
	LBLPASSWORD = (By.XPATH, '//*[contains(text(), "Password")]')
	LBLREMEMBER = (By.CLASS_NAME, 'form-check-label')
	ICNUSER = (By.XPATH, '//div[starts-with(@class, "pre-icon os-icon os-icon-user-male-circle")]')
	ICNPWD = (By.XPATH, '//div[starts-with(@class, "pre-icon os-icon os-icon-fingerprint")]')
	ALERT = (By.XPATH, '//*[starts-with(@id, "random")]')


	# locators for textboxes, button and checkboxes
	TXTUSERNAME = (By.ID, 'username')
	TXTPASSWORD = (By.ID, 'password')
	BTNLOGIN = (By.XPATH, '//*[@id="log-in"]')
	CHKREMEMBER = (By.CLASS_NAME, 'form-check-input')

	# locators for image icons
	IMGTWITTER = (By.XPATH, '//img[contains(@src, "img/social-icons/twitter.png")]')
	IMGFACEBOOK = (By.XPATH, '//img[contains(@src, "img/social-icons/facebook.png")]')
	IMGLINKEDIN = (By.XPATH, '//img[contains(@src, "img/social-icons/linkedin.png")]')

#Locators for HomePage


