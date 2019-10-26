#! /usr/bin/python
# - * - coding: UTF - 8 - * -
from log import record
URL = 'URL'
IP = 'IP'
TITLE = '文章标题'
VISITS = '访问次数'
ACCESS_IP_NUM = '访问IP数'
ARTICLES_NUM = '访问文章数'


class LogReport(object):
    def __init__(self, data):
        self.data = data

    def article_report(self):
        """

        :return: 文章报表
        """
        info = [URL, TITLE, VISITS, ACCESS_IP_NUM]
        self.print_info(info)
        for url, value in self.data['url_data'].items():
            title = None
            if value['title']:
                title = value['title'].decode('utf-8').encode('GBK')
            print("| {} | {} |{} | {} |".format(url, title, value['num'], len(value['ip'])))

    def ip_report(self):
        """

        :return: IP报表
        """
        info = [IP, VISITS, ARTICLES_NUM]
        self.print_info(info)
        for ip, count in self.data['ip_data'].items():
            print("| {} | {} | {} |".format(ip, count['num'], len(count['article'])))

    def full_report(self):
        """

        :return: 完整报表
        """
        info = [IP, URL, VISITS]
        self.print_info(info)
        for ip, count in self.data['ip_data'].items():
            for url in count['article']:
                print("| {} | {} | {} |".format(ip, url, count[url]))

    def all_report(self):
        """

        :return: 全部报表
        """
        self.article_report()
        self.ip_report()
        self.full_report()

    def print_info(self, info):
        """

        :param info: 输出表字段
        :return: 输出表字段信息
        """
        print_info = ''
        separator = ''
        for data in info:
            res = ' ' + data + ' '
            print_info = print_info + "|" + res
            separator = separator + "|" + '-' * len(res)

        print print_info.decode('utf-8').encode('GBK') + '|'
        print separator + '|'
