# - * - coding: UTF - 8 - * -
import unittest

from analyzer.log import crawler
from analyzer.tests.unit.log.crawler import fake_data


class TestCrawler(unittest.TestCase):
    def test_get_title(self):
        exp_value = fake_data.get_title_ret
        act_value = crawler.get_title(fake_data.url)
        self.assertEqual(exp_value, act_value)

    def test_get_title_failed(self):
        exp_value = fake_data.get_title_failed_ret
        act_value = crawler.get_title(fake_data.url_error)
        self.assertEqual(exp_value, act_value)
