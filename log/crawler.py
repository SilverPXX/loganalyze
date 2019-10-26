# - * - coding: UTF - 8 - * -
import urllib2
from urllib2 import HTTPError
from urllib2 import URLError
from bs4 import BeautifulSoup


def get_title(url):
    """

    :param url: 需要获取标题的url
    :return: 成功 文章标题  失败 None
    """
    try:
        html = urllib2.urlopen(url)
    except (HTTPError, URLError):
        return None
    try:
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.text
    except AttributeError:
        return None
    return title
