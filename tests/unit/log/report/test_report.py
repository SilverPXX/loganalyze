# - * - coding: UTF - 8 - * -
import unittest
import mock

from analyzer.log import report
from analyzer.tests.unit.log.report import fake_data


class TestLogReport(unittest.TestCase):
    def setUp(self):
        self.report = report.LogReport(fake_data.log_data)

    @mock.patch('analyzer.log.report.LogReport.print_info')
    def test_article_report(self, mock_print_info):
        mock_print_info.return_value = None
        exp_value = fake_data.article_report_ret
        act_value = self.report.article_report()
        self.assertEqual(exp_value, act_value)

    @mock.patch('analyzer.log.report.LogReport.print_info')
    def test_ip_report(self, mock_print_info):
        mock_print_info.return_value = None
        exp_value = fake_data.ip_report_ret
        act_value = self.report.ip_report()
        self.assertEqual(exp_value, act_value)

    @mock.patch('analyzer.log.report.LogReport.print_info')
    def test_full_report(self, mock_print_info):
        mock_print_info.return_value = None
        exp_value = fake_data.full_report_ret
        act_value = self.report.full_report()
        self.assertEqual(exp_value, act_value)

    def test_print_info(self):
        exp_value = fake_data.print_info_ret
        act_value = self.report.print_info(fake_data.print_info)
        self.assertEqual(exp_value, act_value)
