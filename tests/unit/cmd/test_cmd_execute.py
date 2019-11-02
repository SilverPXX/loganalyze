# - * - coding: UTF - 8 - * -
import unittest

from analyzer.cmd.cmd_execute import ExecuteCmd
from analyzer.tests.unit.cmd import fake_data
from analyzer.cmd import exception


class TestCmdExecute(unittest.TestCase):
    def setUp(self):
        self.execute = ExecuteCmd()

    def test_is_ipv4(self):
        act_value = self.execute.is_ipv4(fake_data.ip_vaild)
        exp_value = fake_data.ip_vaild_ret
        self.assertEqual(exp_value, act_value)

    def test_is_not_ipv4(self):
        act_value = self.execute.is_ipv4(fake_data.ip_invaild)
        exp_value = fake_data.ip_invaild_ret
        self.assertEqual(exp_value, act_value)

    def test_is_domain(self):
        act_value = self.execute.is_domain(fake_data.domain_vaild)
        exp_value = fake_data.domain_vaild_ret
        self.assertEqual(exp_value, act_value)

    def test_is_not_domain(self):
        act_value = self.execute.is_domain(fake_data.domain_invaild)
        exp_value = fake_data.domain_invaild_ret
        self.assertEqual(exp_value, act_value)
