import unittest
from selenium import webdriver


class MadlibFunctionalTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_compliment(self):
        self.driver.get('http://localhost:5000/hello')
        el = self.driver.find_element_by_name('person')
        el.send_keys('Test User')
        self.driver.find_element_by_xpath('//form/input[1]').click()

        assert 'Test User' in self.driver.page_source


if __name__ == '__main__':
    unittest.main()
