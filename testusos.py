import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()

    def tearDown(self):
        self.driver.close()

class InputTesting(TestCase):
    BLOG_URL = ("https://login.pwr.edu.pl/auth/realms/pwr.edu.pl/protocol/cas/login?service=https%3A%2F%2Fweb.usos.pwr.edu.pl%2Fkontroler.php%3F_action%3Dlogowaniecas%2Findex%26callback%3DK7YyNrVS0s%252FOzyspys9JLdIryCiwj09MLsnMz7PNSy0v1k9JTUsszSlRsgYAf7d07a0207631b604331dd53d3aa869cf9ee373b&locale=pl")
    INPUT_NAME = "username"
    BUTTON_NAME = "clear"

    def test_input_value(self):
        self.driver.get(self.BLOG_URL)
        try:
            login_box = self.driver.find_element (by = By.NAME, value = self.INPUT_NAME)
        except Exception:
            self.fail("Login input not found!")

        login_box.send_keys("your_username")
        inputValue = login_box.get_attribute ("value")
        self.assertEqual("your_username",inputValue)

    def test_clear_button(self):
        self.driver.get(self.BLOG_URL)
        try:
            login_box = self.driver.find_element(by=By.NAME, value=self.INPUT_NAME)
            clear_box = self.driver.find_element (by = By.NAME, value = self.BUTTON_NAME)
        except Exception:
            self.fail("Login input not found!")

        login_box.send_keys("your_username")
        clear_box.click()
        inputValue = login_box.get_attribute("value")
        self.assertEqual("", inputValue)

if __name__ == '__main__':
    unittest.main()