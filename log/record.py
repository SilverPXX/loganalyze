# - * - coding: UTF - 8 - * -
import logging
from collections import defaultdict

from analyzer.log import exception
from analyzer.common import logger
from analyzer.log import parse
from analyzer.log import crawler

LOG = logging.getLogger(__name__)
logger.log_handler(LOG)

# 期望保留页面、文档、媒体类型
EXCEPT_RESOURCE = ['.html', 'htm', 'pdf', 'doc', 'docx', 'mpg']

HTTP = 'http://'


class LogRecord(object):
    """ 日志记录类 """
    def __init__(self, logs):
        self.logs = logs

    def record_url(self, server_ip=None):
        """
        获取包括文章标题的数据
        :param server_ip: 请求服务端的ip地址
        :return: 包括文章标题的url相关数据
        """
        url_data = self.url_data()
        return self.get_title(url_data, server_ip)

    def record_ip(self):
        """
        获取ip的数据
        :return: ip的相关数据
        """
        ip_data = defaultdict(defaultdict)
        for log in self.logs:
            if not log:
                continue
            ip = log['remote_addr']
            url = log['request']['url']
            # # 只保留页面、文档、媒体类型访问
            for resource in EXCEPT_RESOURCE:
                if url.endswith(resource):
                    ip_data[ip].setdefault('num', 0)
                    ip_data[ip]['num'] += 1
                    ip_data[ip].setdefault('article', set())
                    ip_data[ip]['article'].add(url)
                    ip_data[ip].setdefault(url, 0)
                    ip_data[ip][url] += 1
        return ip_data

    def url_data(self):
        """
        获取url的数据
        :return: 包括url的访问次数，访问ip数
        """
        url_data = defaultdict(defaultdict)
        for log in self.logs:
            if not log:
                continue
            ip = log['remote_addr']
            url = log['request']['url']
            # 只保留页面、文档、媒体类型访问
            for resource in EXCEPT_RESOURCE:
                if url.endswith(resource):
                    url_data[url].setdefault('num', 0)
                    url_data[url]['num'] += 1
                    url_data[url].setdefault('ip', set())
                    url_data[url]['ip'].add(ip)

        return url_data

    @staticmethod
    def get_title(url_data, server_ip=None):
        """
        获取包括文章标题的url数据
        :param url_data: 包括url的访问次数，访问ip数
        :param server_ip: 请求的服务器ip
        :return: 包括文章标题的url相关数据
        """
        for url in url_data.keys():
            url_data[url].setdefault('title', None)
            if server_ip:
                req = HTTP + server_ip + url
                url_data[url]['title'] = crawler.get_title(req)

        return url_data


def record_data(log_file, server_ip=None):
    # 1.获取到日志文件数据
    log_data = parse.LogParse(log_file)
    if not any(log_data):
        LOG.error('file(%s) log data does not exist' % log_file)
        raise exception.LogNotExists()
    # 2.记录url和ip的相关数据
    record = LogRecord(log_data)
    return dict(url_data=record.record_url(server_ip), ip_data=record.record_ip())
