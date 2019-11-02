#! /usr/bin/python
# - * - coding: UTF - 8 - * -
import logging

from analyzer import exception
from analyzer.common import logger
from analyzer.cmd import cmd_parse
from analyzer.log import parse
from analyzer.log import record
from analyzer.log import report

LOG = logging.getLogger(__name__)
logger.log_handler(LOG)


class ExecuteCmd(object):
    def __init__(self):
        self.log_report = ''
        self.pre_check_cmd = cmd_parse.PreCheckCmd()

    def execute_cmd(self, args):
        LOG.info('execute_cmd params: log_file: %s, url: %s, type: %s',
                 args.log_file, args.url, args.type)
        # 1. 检查输入url的合法性
        self.pre_check_cmd.check_vaild(args.url)
        # 2. 记录url和ip的数据
        log_data = self.record_data(args.log_file, args.url)
        # 3.输出相关报表
        self.log_report = report.LogReport(log_data)
        report_dict = self.report_dict()
        for report_type in args.type:
            report_dict[report_type]()

    def report_dict(self):
        all = self.log_report.all_report
        article = self.log_report.article_report
        ip = self.log_report.ip_report
        full = self.log_report.full_report
        return dict(all=all, article=article, ip=ip, full=full)

    @staticmethod
    def record_data(log_file, server_ip=None):
        # 1.获取到日志文件数据
        log_data = parse.LogParse(log_file)
        if not any(log_data):
            LOG.error('file(%s) log data does not exist' % log_file)
            raise exception.LogNotExists(log_file)
        # 2.记录url和ip的相关数据
        record_data = record.LogRecord(log_data)
        return dict(url_data=record_data.record_url(server_ip), ip_data=record_data.record_ip())


def main():
    args = cmd_parse.parse_cmd()
    cmd = ExecuteCmd()
    cmd.execute_cmd(args)


if __name__ == "__main__":
    main()

