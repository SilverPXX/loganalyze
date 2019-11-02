# - * - coding: UTF - 8 - * -
import unittest

from analyzer.log.record import LogRecord
from analyzer.tests.unit.log.record import fake_data


class TestLogRecord(unittest.TestCase):

    def test_url_data(self):
        record = LogRecord(fake_data.load_file_ret)
        act_value = record.url_data()
        exp_value = fake_data.url_data_ret
        self.assertEqual(exp_value, act_value)

    def test_get_title(self):
        record = LogRecord(fake_data.load_file_ret)
        url_data = fake_data.url_data
        exp_value = fake_data.get_title_ret
        act_value = record.get_title(url_data)
        self.assertEqual(exp_value, act_value)

    def test_get_title_server_ip(self):
        record = LogRecord(fake_data.load_file_ret)
        url_data = fake_data.url_data
        exp_value = fake_data.get_title_server_ip_ret
        act_value = record.get_title(url_data, fake_data.server_ip)
        self.assertEqual(exp_value, act_value)

    def test_record_ip(self):
        record = LogRecord(fake_data.load_file_ret)
        act_value = record.record_ip()
        exp_value = fake_data.ip_data_ret
        self.assertEqual(exp_value, act_value)
