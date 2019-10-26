# - * - coding: UTF - 8 - * -

log_data = {
    'ip_data': {
        '177.1.81.42': {
            'article': set([
                '/designing/tools/image/UML_classes.docx',
            ]),
            'num': 3,
            '/designing/tools/image/UML_classes.docx': 1,
        },
        '200.200.76.130': {
            'article': set([
                '/coding/miniprj/material.html',
            ]),
            'num': 3,
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
            'title': '今日头条'
        },
        '/designing/tools/image/UML_classes.docx': {
            'ip': set(['177.1.81.42']),
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
