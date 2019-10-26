# - * - coding: UTF - 8 - * -

log_data = {
    'ip_data': {
        '177.1.81.42': {
            'article': set([
                '/designing/tools/image/gitbook/images/favicon.ico',
                '/designing/tools/image/UML_classes.docx',
                '/designing/tools/image/favicon.ico'
            ]),
            'num': 3,
            '/designing/tools/image/gitbook/images/favicon.ico': 1,
            '/designing/tools/image/UML_classes.docx': 1,
            '/designing/tools/image/favicon.ico': 1
        },
        '200.200.76.130': {
            'article': set([
                '/coding/style/%E7%BC%96%E7%A0%81%E9%A3%8E%E6%A0%BC.zip',
                '/coding/miniprj/material.html',
                '/coding/gitbook/fonts/fontawesome/fontawesome-webfont.woff2?v=4.6.3'
            ]),
            'num': 3,
            '/coding/gitbook/fonts/fontawesome/fontawesome-webfont.woff2?v=4.6.3': 1,
            '/coding/style/%E7%BC%96%E7%A0%81%E9%A3%8E%E6%A0%BC.zip': 1,
            '/coding/miniprj/material.html': 1,
        },
        '::1': {
            'article': set(['*']),
            'num': 1,
            '*': 1
        },
    },
    'url_data': {
        '/coding/miniprj/material.html': {
            'ip': set(['200.200.76.130']),
            'num': 1,
            'title': None
        },
        '/designing/tools/image/UML_classes.docx': {
            'ip': set(['177.1.81.42']),
            'num': 1,
            'title': None
        },
        '*': {
            'ip': set(['::1']),
            'num': 1,
            'title': None
        },
        '/designing/tools/image/gitbook/images/favicon.ico': {
            'ip': set(['177.1.81.42']),
            'num': 1,
            'title': None
        },
        '/coding/gitbook/fonts/fontawesome/fontawesome-webfont.woff2?v=4.6.3': {
            'ip': set(['200.200.76.130']),
            'num': 1,
            'title': None
        },
        '/designing/tools/image/favicon.ico': {
            'ip': set(['177.1.81.42']),
            'num': 1,
            'title': None
        },
        '/coding/style/%E7%BC%96%E7%A0%81%E9%A3%8E%E6%A0%BC.zip': {
            'ip': set(['200.200.76.130']),
            'num': 1,
            'title': None
        }
    }
}

article_report_ret = None

ip_report_ret = None

full_report_ret = None

print_info_ret = None

print_info = ['URL', '文章标题', '访问次数', '访问IP数']