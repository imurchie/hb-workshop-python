import unittest
from selenium import webdriver



class MadlibFunctionalTests(unittest.TestCase):
    host = 'http://localhost:5000/%s'

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        # self.driver = webdriver.Safari()

    def tearDown(self):
        self.driver.close()

    def test_compliment(self):
        name = 'Test User'
        self.driver.get(self.host % 'hello')
        el = self.driver.find_element_by_name('person')
        el.send_keys(name)
        self.driver.find_element_by_xpath('//form/input[1]').click()

        assert name in self.driver.page_source

    def test_no_game(self):
        self.test_compliment()
        self.driver.find_element_by_css_selector("input[type='radio'][value='no']").click()
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        assert 'Bye!' in self.driver.page_source

    @unittest.skip('fill this in, and unskip!')
    def test_game(self):
        pass


if __name__ == '__main__':
    unittest.main()
