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

    def test_add_url(self):
        self.spyder.add_url("http://gocardless.com/faq")
        self.assertEquals(len(self.spyder.to_crawl), 1)

    def test_add_existing_url(self):
        self.spyder.add_url("http://gocardless.com/faq")
        self.spyder.add_url("/faq")
        self.assertEqual(len(self.spyder.to_crawl), 1)

    def test_add_excluded_url(self):
        result = self.spyder.add_url("http://gocardless.com/notallowed.pdf")
        self.assertEqual(result, None)
