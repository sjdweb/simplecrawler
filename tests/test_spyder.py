import unittest
from crawler.spyder import Spyder


class SpyderTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://gocardless.com"
        self.spyder = Spyder(self.base_url)

    def test_base_url(self):
        self.assertEqual(self.spyder.base_url, self.base_url)

    def test_get_url(self):
        result = self.spyder.get_url("http://gocardless.com")
        self.assertIsNotNone(result)
