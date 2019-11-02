# - * - coding: UTF - 8 - * -
import re
import logging

from analyzer.common import logger
from analyzer.log import report
from analyzer.log import record
from analyzer.cmd import exception

LOG = logging.getLogger(__name__)
logger.log_handler(LOG)


class ExecuteCmd(object):
    def __init__(self):
        self.log_report = ''

    def execute_cmd(self, args):
        LOG.info('execute_cmd params: log_file: %s, url: %s, type: %s',
                 args.log_file, args.url, args.type)
        self.check_vaild(args.url)
        log_data = record.record_data(args.log_file, args.url)
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
    def is_ipv4(ip):
        ipv4_regex = re.compile(
            r'(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)(?:\.(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}',
            re.IGNORECASE)
        if ip and not ipv4_regex.match(ip):
            return False
        return True

    @staticmethod
    def is_domain(domain):
        domain_regex = re.compile(
            r'(?:[A-Z0-9_](?:[A-Z0-9-_]{0,247}[A-Z0-9])?\.)+(?:[A-Z]{2,6}|[A-Z0-9-]{2,}(?<!-))(:[0-9]+)?\Z',
            re.IGNORECASE)
        if domain and not domain_regex.match(domain):
            return False
        return True

    def check_vaild(self, url):
        if not (self.is_ipv4(url) or self.is_domain(url)):
            LOG.error("the input url(%s) is illegal")
            raise exception.UrlInvaild(url)
