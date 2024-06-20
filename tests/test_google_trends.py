import unittest
from src.google_trends import get_google_trends

class TestGoogleTrends(unittest.TestCase):
    def test_get_google_trends(self):
        keywords = ["custom cutting boards"]
        result = get_google_trends(keywords)
        self.assertIsNotNone(result)
        
if __name__ == "__main__":
    unittest.main()
