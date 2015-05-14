import os
import sys
import unittest
from selenium import webdriver

USERNAME = os.environ.get('SAUCE_USERNAME')
ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')
sauce = SauceClient(USERNAME, ACCESS_KEY)

browsers = [{
                "platform": "OS X 10.10",
                "browserName": "chrome",
                "version": "38"
            },
            {
                "platform": "OS X 10.10",
                "browserName": "Safari",
                "version": "8.0"
            },
            {
                "platform": "Windows 8.1",
                "browserName": "internet explorer",
                "version": "11"
            },]


def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)
    return decorator


class MadlibFunctionalTests(unittest.TestCase):
    host = 'http://localhost:5000/%s'

    def setUp(self):
        self.desired_capabilities['name'] = self.id()

        sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
        self.driver = webdriver.Remote(
            desired_capabilities=self.desired_capabilities,
            command_executor=sauce_url % (USERNAME, ACCESS_KEY)
        )
        self.driver.implicitly_wait(30)


    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        try:
            if sys.exc_info() == (None, None, None):
                sauce.jobs.update_job(self.driver.session_id, passed=True)
            else:
                sauce.jobs.update_job(self.driver.session_id, passed=False)
        finally:
            self.driver.quit()

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
