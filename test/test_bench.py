import unittest
from scripts.bench import ENDPOINTS

class BenchTest(unittest.TestCase):
    def test_endpoints_are_clean_https(self):
        self.assertGreaterEqual(len(ENDPOINTS), 5)
        for url in ENDPOINTS:
            self.assertTrue(url.startswith("https://"))
            self.assertNotIn("shinnslist", url)

if __name__ == "__main__":
    unittest.main()
