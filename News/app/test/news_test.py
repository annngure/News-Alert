import unittest
from models import news
NEWS=news.NEWS

class NewsTest(unittest.TestCase):
    '''
    Test Class to the behaviour of the News class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_NEWS = NEWS("DANGER","NO NEWS",123)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_NEWS,NEWS))   

if __name__='__main__':
    unittest.main()
    

