# - * - coding: UTF - 8 - * -
import sys
import os
import unittest

from analyzer.cmd import cmd_parse
from analyzer.tests.unit.cmd import fake_data


class TestCmdParse(unittest.TestCase):

    def test_get_title(self):
        sys.argv.append('--log_file=apache.log')
        sys.argv.append('--url=200.200.1.35')
        sys.argv.append('--type=all')
        args = cmd_parse.parse_cmd()
        act_value = (args.log_file, args.url, args.type)
        exp_value = ('apache.log', '200.200.1.35', ['all'])
        self.assertEqual(exp_value, act_value)


class TestPreCheckCmd(unittest.TestCase):
    def setUp(self):
        self.pre_check = cmd_parse.PreCheckCmd()

    def test_is_ipv4(self):
        act_value = self.pre_check.is_ipv4(fake_data.ip_vaild)
        exp_value = fake_data.ip_vaild_ret
        self.assertEqual(exp_value, act_value)

    def test_is_not_ipv4(self):
        act_value = self.pre_check.is_ipv4(fake_data.ip_invaild)
        exp_value = fake_data.ip_invaild_ret
        self.assertEqual(exp_value, act_value)

    def test_is_domain(self):
        act_value = self.pre_check.is_domain(fake_data.domain_vaild)
        exp_value = fake_data.domain_vaild_ret
        self.assertEqual(exp_value, act_value)

    def test_is_not_domain(self):
        act_value = self.pre_check.is_domain(fake_data.domain_invaild)
        exp_value = fake_data.domain_invaild_ret
        self.assertEqual(exp_value, act_value)
