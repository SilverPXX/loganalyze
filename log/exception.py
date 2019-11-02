# - * - coding: UTF - 8 - * -


class LogNotExists(Exception):

    def __str__(self):
        mesg = u"日志数据不存在，请确认日志文件是否正确！"
        return mesg.decode('utf-8').encode('GBK')
