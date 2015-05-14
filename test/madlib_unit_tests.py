import sys, os
from os import path
sys.path.append(path.dirname(path.dirname( path.abspath(__file__) )))
import madlibs
import unittest


class MadlibUnitTests(unittest.TestCase):

    def setUp(self):
        madlibs.app.config['TESTING'] = True
        self.app = madlibs.app.test_client()

    def tearDown(self):
        pass

    def test_start_here(self):
        res = self.app.get('/')
        assert 'Hi! This is the home page.' == res.data

    def test_say_hello(self):
        res = self.app.get('/hello')
        assert 'Hi There!' in res.data
        assert 'What\'s your name' in res.data

    def test_greet_person_no_data(self):
        res = self.app.post('/greet')
        assert 'Anonymous person' in res.data

    def test_greet_person(self):
        res = self.app.post('/greet', data=dict(person='Test User'))
        assert 'Test User' in res.data

    @unittest.skip('fill this in, and unskip!')
    def test_show_game_form(self):
        pass

    @unittest.skip('fill this in, and unskip!')
    def test_show_madlib(self):
        pass


if __name__ == '__main__':
    unittest.main()
