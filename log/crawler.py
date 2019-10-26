# - * - coding: UTF - 8 - * -
import urllib2
from urllib2 import HTTPError
from urllib2 import URLError
import re


def get_title(url):
    try:
        html = urllib2.urlopen(url).read()
        res_list = re.findall(r"<title>.*\s?.*</title>", html)
        if not res_list:
            return None
        return res_list[0][7:-8]
    except (HTTPError, URLError):
        return None
