# - * - coding: UTF - 8 - * -
import re
import logging

from analyzer.common import logger

LOG = logging.getLogger(__name__)
logger.log_handler(LOG)

ops = {
    'datetime': str,
    'request': lambda request: dict(zip(('method', 'url', 'protocol'), request.split())),
    'status': int,
    'size': int
}


class LogParse(object):
    """
    解析日志文件类
    """
    def __init__(self, path):
        self.log_path = path

    def __iter__(self):
        with open(self.log_path) as log:
            for line in log:
                yield self._parse_log(line)

    @staticmethod
    def _parse_log(line):
        """
        解析单行日志信息
        :param line: 单行日志信息
        :return: 返回日志结构
        """
        pattern = r'(?P<remote_addr>[\d\.]{7,})' \
                  r' - - ' \
                  r'(?:\[(?P<datetime>[^\[\]]+)\])' \
                  r' "(?P<request>[^"]+)" ' \
                  r'(?P<status>\d+) ' \
                  r'(?P<size>\d+)'
        regex = re.compile(pattern)
        matcher = regex.match(line)
        if matcher:
            return {key: ops.get(key, lambda x: x)(val) for key, val in matcher.groupdict().items()}
