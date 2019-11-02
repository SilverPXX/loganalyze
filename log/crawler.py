# - * - coding: UTF - 8 - * -
import logging
import urllib2
from urllib2 import HTTPError
from urllib2 import URLError
from bs4 import BeautifulSoup

from analyzer.common import logger

LOG = logging.getLogger(__name__)
logger.log_handler(LOG)


def get_title(url):
    """
    获取文章标题
    :param url: 需要获取标题的url
    :return: 成功 文章标题  失败 None
    """
    try:
        html = urllib2.urlopen(url)
    except (HTTPError, URLError) as ex:
        LOG.warn('get url(%s) title failed, err: %s', url, ex)
        return None
    try:
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.text
    except AttributeError as ex:
        LOG.warn('get url(%s) title failed, err: %s', url, ex)
        return None
    return title
