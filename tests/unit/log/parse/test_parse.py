# - * - coding: UTF - 8 - * -
import unittest

from analyzer.log import parse
from analyzer.tests.unit.log.parse import fake_data


class TestLogParse(unittest.TestCase):
    def setUp(self):
        self.parse = parse.LogParse('')

    def test_parse_log(self):
        act_value = self.parse._parse_log(fake_data.single_log)
        exp_value = fake_data.parse_log_ret
        self.assertEqual(exp_value, act_value)
