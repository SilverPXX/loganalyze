# - * - coding: UTF - 8 - * -
import sys
import os
import unittest

from analyzer.cmd import cmd_parse


class TestCmdParse(unittest.TestCase):

    def test_get_title(self):
        sys.argv.append('--log_file=apache.log')
        sys.argv.append('--url=200.200.1.35')
        sys.argv.append('--type=all')
        args = cmd_parse.parse_cmd()
        act_value = (args.log_file, args.url, args.type)
        exp_value = ('apache.log', '200.200.1.35', ['all'])
        self.assertEqual(exp_value, act_value)
