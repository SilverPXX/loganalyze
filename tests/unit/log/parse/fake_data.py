# - * - coding: UTF - 8 - * -


single_log = '200.200.76.130 - - [16/Feb/2019:11:27:20 +0800] "GET /coding/miniprj/material.html HTTP/1.1" 200 38093'

parse_log_ret = {
    'status': 200,
    'datetime': '16/Feb/2019:11:27:20 +0800',
    'remote_addr': '200.200.76.130',
    'request': {
        'url': '/coding/miniprj/material.html',
        'protocol': 'HTTP/1.1',
        'method': 'GET'
    },
    'size': 38093
}
