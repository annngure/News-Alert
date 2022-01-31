import unittest
from models import news
News=news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news=News(9898,'Danger Ahead!','Sign that is put up but nobody follows','https://img.news.org/50/500',45,23)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
if __name__=='__main__':
    unittest.main()
