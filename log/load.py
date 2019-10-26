# - * - coding: UTF - 8 - * -


class LoadFile(object):
    """
    导入日志文件类
    """
    def __init__(self, path):
        self.log_path = path

    def __iter__(self):
        with open(self.log_path) as log:
            for line in log:
                yield self.__struct(line)

    def __struct(self, single_log):
        """

        :param single_log: 单行日志
        :return: 日志数据字典
        """
        log_data = single_log.split()
        ip = log_data[0]
        date = log_data[3] + ' ' + log_data[4]
        method = log_data[5]
        url = log_data[6]
        protocol = log_data[7]
        status = log_data[8]
        byte = log_data[9]
        return dict(ip=ip, date=date, method=method, url=url,
                    protocol=protocol, status=status, byte=byte)
