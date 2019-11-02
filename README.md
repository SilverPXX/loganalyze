# APACHE日志分析

## 使用方法和结果

### 程序

#### 使用方法

> python main.py -h
```
usage: main.py [-h] -f LOG_FILE -t {all,ip,article,full} [-i IP]

optional arguments:
  -h, --help            show this help message and exit
  -f LOG_FILE, --log_file LOG_FILE
                        log file path
  -t {all,ip,article,full}, --type {all,ip,article,full}
                        output report type
  -i IP, --ip IP        log source ip

example: python main.py -f D:\\apache.log -t article -u 200.200.1.35
```

#### 结果

> python main.py -f D:\\apache.log -t all -t full -u 200.200.1.35
```

| URL | 文章标题 | 访问次数 | 访问IP数 |
|-----|--------------|--------------|-------------|
| /coding/miniprj/material.html | 培训素材 · 编码上手包 |1 | 1 |
| /designing/tools/image/UML_classes.docx | None |1 | 1 |

| IP | 访问次数 | 访问文章数 |
|----|--------------|-----------------|
| 177.1.81.42 | 1 | 1 |
| 200.200.76.130 | 1 | 1 |

| IP | URL | 访问次数 |
|----|-----|--------------|
| 177.1.81.42 | /designing/tools/image/UML_classes.docx | 1 |
| 200.200.76.130 | /coding/miniprj/material.html | 1 |

F:\Persis\SANGFOR\analyzer>python main.py -f E:\\apache.log -t all -t full -u 200.200.1.35
No handlers could be found for logger "bs4.dammit"

| URL | 文章标题 | 访问次数 | 访问IP数 |
|-----|--------------|--------------|-------------|
| /coding/miniprj/material.html | 培训素材 · 编码上手包 |1 | 1 |
| /designing/tools/image/UML_classes.docx | None |1 | 1 |

| IP | 访问次数 | 访问文章数 |
|----|--------------|-----------------|
| 177.1.81.42 | 1 | 1 |
| 200.200.76.130 | 1 | 1 |

| IP | URL | 访问次数 |
|----|-----|--------------|
| 177.1.81.42 | /designing/tools/image/UML_classes.docx | 1 |
| 200.200.76.130 | /coding/miniprj/material.html | 1 |

| IP | URL | 访问次数 |
|----|-----|--------------|
| 177.1.81.42 | /designing/tools/image/UML_classes.docx | 1 |
| 200.200.76.130 | /coding/miniprj/material.html | 1 |
```

### 单测

#### 使用方法
> pytest
```
在项目根目录下执行pytest即可
```

#### 结果
> pytest
```
============================= test session starts =============================
platform win32 -- Python 2.7.15, pytest-4.6.6, py-1.8.0, pluggy-0.13.0
rootdir: F:\Persis\SANGFOR\analyzer
plugins: cov-2.8.1
collected 16 items

tests\unit\cmd\test_cmd_parse.py .....                                   [ 31%]
tests\unit\log\crawler\test_crawler.py ..                                [ 43%]
tests\unit\log\parse\test_parse.py .                                     [ 50%]
tests\unit\log\record\test_record.py ....                                [ 75%]
tests\unit\log\report\test_report.py ....                                [100%]

========================== 16 passed in 0.77 seconds ==========================
```

### 单测覆盖率

#### 使用方法
>pytest --cov ./
```
在项目根目录下执行pytest --cov ./
```

#### 结果

> pytest --cov ./
```
============================= test session starts =============================
platform win32 -- Python 2.7.15, pytest-4.6.6, py-1.8.0, pluggy-0.13.0
rootdir: F:\Persis\SANGFOR\analyzer
plugins: cov-2.8.1
collected 16 items

tests\unit\cmd\test_cmd_parse.py .....                                   [ 31%]
tests\unit\log\crawler\test_crawler.py ..                                [ 43%]
tests\unit\log\parse\test_parse.py .                                     [ 50%]
tests\unit\log\record\test_record.py ....                                [ 75%]
tests\unit\log\report\test_report.py ....                                [100%]

---------- coverage: platform win32, python 2.7.15-final-0 -----------
Name                                     Stmts   Miss  Cover
------------------------------------------------------------
__init__.py                                  0      0   100%
cmd\__init__.py                              0      0   100%
cmd\cmd_parse.py                            30      3    90%
cmd\exception.py                             6      3    50%
common\__init__.py                           0      0   100%
common\logger.py                             8      0   100%
exception.py                                 6      3    50%
log\__init__.py                              3      0   100%
log\crawler.py                              21      0   100%
log\parse.py                                19      3    84%
log\record.py                               52      2    96%
log\report.py                               42      3    93%
main.py                                     41     41     0%
tests\__init__.py                            0      0   100%
tests\unit\__init__.py                       0      0   100%
tests\unit\cmd\__init__.py                   0      0   100%
tests\unit\cmd\fake_data.py                  8      0   100%
tests\unit\cmd\test_cmd_parse.py            33      0   100%
tests\unit\log\__init__.py                   0      0   100%
tests\unit\log\crawler\__init__.py           0      0   100%
tests\unit\log\crawler\fake_data.py          4      0   100%
tests\unit\log\crawler\test_crawler.py      12      0   100%
tests\unit\log\parse\__init__.py             0      0   100%
tests\unit\log\parse\fake_data.py            4      0   100%
tests\unit\log\parse\test_parse.py          13      0   100%
tests\unit\log\record\__init__.py            0      0   100%
tests\unit\log\record\fake_data.py           7      0   100%
tests\unit\log\record\test_record.py        27      0   100%
tests\unit\log\report\__init__.py            0      0   100%
tests\unit\log\report\fake_data.py           6      0   100%
tests\unit\log\report\test_report.py        26      0   100%
------------------------------------------------------------
TOTAL                                      368     58    84%


========================== 16 passed in 2.06 seconds ==========================
```
