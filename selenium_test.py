import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class GoogleTestCase(unittest.TestCase):
    options = webdriver.ChromeOptions()

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )

    def setUp(self):
        self.addCleanup(self.driver.quit)

    def test_page_title(self):
        self.driver.get('https://utm.ro')
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, 'CONTACT').click()
        self.driver.save_screenshot('screenshot.png')
        time.sleep(5)
        self.assertIn('Contact - Universitatea Titu Maiorescu', self.driver.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
