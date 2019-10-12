#! /usr/bin/python
# - * - coding: UTF - 8 - * -
import analysis


class LogReport(object):
    def __init__(self, input_file):
        self.log = analysis.LogParse()
        self.url_data, self.ip_data = self.log.log_parse(input_file)

    def article_report(self):
        """ 文章报表 """
        print("| URL | 访问次数 | 访问IP数 |")
        print("|----|----------|-----------|")
        for url, count in self.url_data.items():
            print("| {} | {} | {} |".format(url, count['num'], len(count['ip'])))

    def ip_report(self):
        """  IP报表 """
        print("\n| IP | 访问次数 | 访问文章数 |")
        print("|----|----------|-----------|")
        for ip, count in self.ip_data.items():
            print("| {} | {} | {} |".format(ip, count['num'], len(count['article'])))

    def full_report(self):
        """ 完整报表 """
        print("\n| IP | URL | 访问次数 |")
        print("|----|-----|---------|")
        for ip, count in self.ip_data.items():
            for url in count['article']:
                print("| {} | {} | {} |".format(ip, url, count[url]))

    def all_report(self):
        """ 全部报表 """
        self.article_report()
        self.ip_report()
        self.full_report()


if __name__ == "__main__":
    report = LogReport('E:\\apache.log')
    report.article_report()
    report.ip_report()
    report.full_report()
    report.all_report()
