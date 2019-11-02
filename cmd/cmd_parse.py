# - * - coding: UTF - 8 - * -
import argparse
import sys
import re
import logging

from analyzer.common import logger
from analyzer.cmd import exception

LOG = logging.getLogger(__name__)
logger.log_handler(LOG)


def parse_cmd():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--log_file', help='log file path',
                        required=True)
    parser.add_argument('-t', '--type', help='output report type',
                        choices=['all', 'ip', 'article', 'full'],
                        action='append', required=True)
    parser.add_argument('-u', '--url', help='log source url')

    flags, unparsed = parser.parse_known_args(sys.argv[1:])
    return flags


class PreCheckCmd(object):
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
        if not self.is_ipv4(url) and not self.is_domain(url):
            LOG.error("the input url(%s) is illegal")
            raise exception.UrlInvaild(url)
