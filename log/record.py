# - * - coding: UTF - 8 - * -
from collections import defaultdict
from log import parse
from log import crawler


class LogRecord(object):
    """ 日志记录类 """
    def __init__(self, logs):
        self.logs = logs

    def record_url(self, server_ip=None):
        url_data = self.url_data()
        return self.get_title(url_data, server_ip)

    def record_ip(self):
        ip_data = defaultdict(defaultdict)
        for log in self.logs:
            ip = log['ip']
            url = log['url']
            if url.endswith(".js") or url.endswith(".css"):
                continue
            ip_data[ip].setdefault('num', 0)
            ip_data[ip]['num'] += 1
            ip_data[ip].setdefault('article', set())
            ip_data[ip]['article'].add(url)
            ip_data[ip].setdefault(url, 0)
            ip_data[ip][url] += 1

        return ip_data

    def url_data(self):
        url_data = defaultdict(defaultdict)
        for log in self.logs:
            ip = log['ip']
            url = log['url']
            # 过滤不需要的数据
            if url.endswith(".js") or url.endswith(".css"):
                continue
            url_data[url].setdefault('num', 0)
            url_data[url]['num'] += 1
            url_data[url].setdefault('ip', set())
            url_data[url]['ip'].add(ip)

        return url_data

    def get_title(self, url_data, server_ip=None):
        for url in url_data.keys():
            url_data[url].setdefault('title', None)
            if server_ip:
                req = 'http://' + server_ip + url
                url_data[url]['title'] = crawler.get_title(req)

        return url_data


def record_data(log_file, server_ip=None):
    log_data = parse.LoadFile(log_file)
    record = LogRecord(log_data)
    return dict(url_data=record.record_url(server_ip), ip_data=record.record_ip())
