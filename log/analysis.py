#! /usr/bin/python
# - * - coding: UTF - 8 - * -
import re
from collections import defaultdict


class LogParse(object):
    """ 日志解析类 """
    def __init__(self):
        self.parse_data = []
        self.ip_data = defaultdict(defaultdict)
        self.url_data = defaultdict(defaultdict)
        self.log_record = LogRecord()

    def log_parse(self, log_path):
        """
        @brief  日志解析
        @param  log_path 输入日志文件路径
        """
        with open(log_path, "r") as log_file:
            while 1:
                line = log_file.readline()
                if not line:
                    break
                # 以空格分隔每一条日志
                res = re.split(" ", line)
                ip = res[0]
                url = res[6]
                # 过滤掉css,js等文件访问
                if url.endswith(".js") or url.endswith(".css"):
                    continue

                self.log_record.record_url(self.url_data, url, ip)
                self.log_record.record_ip(self.ip_data, url, ip)

        return self.url_data, self.ip_data


class LogRecord(object):
    """ 日志记录类 """

    def record_url(self, url_data, url, ip):
        url_data[url].setdefault('num', 0)
        url_data[url]['num'] += 1
        url_data[url].setdefault('ip', set())
        url_data[url]['ip'].add(ip)

    def record_ip(self, ip_data, url, ip):
        ip_data[ip].setdefault('num', 0)
        ip_data[ip]['num'] += 1
        ip_data[ip].setdefault('article', set())
        ip_data[ip]['article'].add(url)
        ip_data[ip].setdefault(url, 0)
        ip_data[ip][url] += 1
