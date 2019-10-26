# - * - coding: UTF - 8 - * -
import unittest

from log import crawler
from tests.unit.log.crawler import fake_data


class TestCrawler(unittest.TestCase):
    def test_get_title(self):
        exp_value = fake_data.get_title_ret
        act_value = crawler.get_title(fake_data.url)
        self.assertEqual(exp_value, act_value)


if __name__ == '__main__':
    unittest.main()
