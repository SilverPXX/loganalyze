# - * - coding: UTF - 8 - * -
import argparse
from log import report
from log import record


class ParseCmd(object):
    def __init__(self):
        self.log_report = ''

    def parse_cmd(self):
        parser = argparse.ArgumentParser()
        # 必选参数，不带连接符
        parser.add_argument('log_file', help='log file path')
        # 可选参数，带连接符
        parser.add_argument('-u', '--url', help='log source url')
        parser.add_argument('-t', '--type', help='output report type',
                            choices=['all', 'ip', 'article', 'full'], action='append')
        return parser.parse_args()

    def execute_cmd(self, args):
        if args.url:
            log_data = record.record_data(args.log_file, args.url)
        else:
            log_data = record.record_data(args.log_file)
        self.log_report = report.LogReport(log_data)
        if args.type:
            report_dict = self.report_dict()
            for report_type in args.type:
                report_dict[report_type]()

    def report_dict(self):
        all = self.log_report.all_report
        article = self.log_report.article_report
        ip = self.log_report.ip_report
        full = self.log_report.full_report
        return dict(all=all, article=article, ip=ip, full=full)
