# - * - coding: UTF - 8 - * -


class UrlInvaild(Exception):
    def __init__(self, url):
        self.url = url

    def __str__(self):
        mesg = u"输入的url({})不合法！".format(repr(self.url))
        return mesg.decode('utf-8').encode('GBK')
