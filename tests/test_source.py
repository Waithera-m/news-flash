import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    
    '''
    Tests  Source class bahavior
    '''
    def setUp(self):

        '''
        Method runs before each testcase
        '''
        self.new_source = Source('"abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','https://abcnews.go.com')

    def test_instance(self):

        '''
        Function tests object instatiation
        '''
        self.assertTrue(isinstance(self.new_source,Source))