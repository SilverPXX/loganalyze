#! /usr/bin/python
# - * - coding: UTF - 8 - * -
import re
from collections import defaultdict


class LogParse(object):
    """ 日志解析类 """
    def __init__(self):
        self.analyze_data = []

    def log_parse(self, input_file):
        """ 日志解析 """
        with open(input_file, "r") as log_file:
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

                single_log = {}
                single_log['ip'] = ip
                single_log['url'] = url
                self.analyze_data.append(single_log)

        return self.analyze_data


if __name__ == "__main__":
    log = LogParse()
    data = log.log_parse('E:\\apache.log')
    print data
