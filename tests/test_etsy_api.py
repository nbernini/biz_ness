import unittest
from src.etsy_api import search_etsy

class TestEtsyAPI(unittest.TestCase):
    def test_search_etsy(self):
        api_key = 'your_api_key'
        search_term = 'custom cutting boards'
        result = search_etsy(api_key, search_term)
        self.assertIsNotNone(result)
        
if __name__ == "__main__":
    unittest.main()
