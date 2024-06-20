import unittest
from src.amazon_api import get_amazon_best_sellers

class TestAmazonAPI(unittest.TestCase):
    def test_get_amazon_best_sellers(self):
        aws_access_key_id = 'your_access_key_id'
        aws_secret_access_key = 'your_secret_access_key'
        search_term = 'custom cutting boards'
        result = get_amazon_best_sellers(aws_access_key_id, aws_secret_access_key, search_term)
        self.assertIsNotNone(result)
        
if __name__ == "__main__":
    unittest.main()
