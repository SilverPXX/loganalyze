# - * - coding: UTF - 8 - * -


class LogNotExists(Exception):
    def __init__(self, log_file):
        self.file = log_file

    def __str__(self):
        mesg = u"文件（{}）日志数据不存在，请确认日志文件是否正确！".format(repr(self.file))
        return mesg.decode('utf-8').encode('GBK')
