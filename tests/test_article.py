import unittest
from app.models import Article

class ItemTest(unittest.TestCase):

    '''
    Tests Item class behavior
    '''
    def setUp(self):

        '''
        Method runs before every test
        '''
        self.new_item = Article('abc-news','Daniel Palmer', 'Coinbase Launches Price Oracle Aimed to Reduce Systemic Risk in the DeFi Space','2020-04-24T08:43:18Z','With around a billions dollars sitting in decentralized finance (DeFi) apps and protocols, Coinbase has started to provide a data feed for cryptocurrency prices to help keep those funds secure','https://www.coindesk.com/coinbase-launches-price-oracle-aimed-to-reduce-systemic-risk-in-the-defi-space','https://images.cointelegraph.com/images/717_aHR0cHM6Ly9zMy5jb2ludGVsZWdyYXBoLmNvbS9zdG9yYWdlL3VwbG9hZHMvdmlldy9jYzRjZDg1ZWNjZTg5MjY0ODg1NWIzMDhlZjc4YzA2Ny5qcGc=.jpg')

    def test_instance(self):

        '''
        Function tests object initialization
        '''
        self.assertTrue(isinstance(self.new_item,Article))