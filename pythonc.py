import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://app.onelogin.com/login")
        email = driver.find_element_by_id("email")
	password = driver.find_element_by_id("password")
	email.send_keys("09460303@itcolima.edu.mx")
	password.send_keys("baster91")
	driver.find_element_by_id("login").click()
	wait = WebDriverWait(driver, 20)
	element = wait.until(EC.element_to_be_clickable((By.ID,'login')))
        

	driver.get("https://app.onelogin.com/users/new")

   

if __name__ == "__main__":
    unittest.main()
