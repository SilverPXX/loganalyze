# APACHE日志分析

## 使用方法和结果

### 程序

#### 使用方法

>python main.py -h
```
usage: main.py [-h] [-u URL] [-t {all,ip,article,full}] log_file

positional arguments:
  log_file              log file path

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     log source url
  -t {all,ip,article,full}, --type {all,ip,article,full}
                        output report type

example: python main.py E:\\apache.log -t article -u 200.200.1.35
```

#### 结果

>F:\Persis\SANGFOR\analyzer>python main.py E:\\apache.log -t article -t all -u isyk.xyz:8001
```
| URL | 文章标题 | 访问次数 | 访问IP数 |
|-----|--------------|--------------|-------------|
| /coding/miniprj/material.html | 今日头条 |1 | 1 |
| /designing/tools/image/UML_classes.docx | None |1 | 1 |
| URL | 文章标题 | 访问次数 | 访问IP数 |
|-----|--------------|--------------|-------------|
| /coding/miniprj/material.html | 今日头条 |1 | 1 |
| /designing/tools/image/UML_classes.docx | None |1 | 1 |
| IP | 访问次数 | 访问文章数 |
|----|--------------|-----------------|
| 177.1.81.42 | 1 | 1 |
| 200.200.76.130 | 1 | 1 |
| IP | URL | 访问次数 |
|----|-----|--------------|
| 177.1.81.42 | /designing/tools/image/UML_classes.docx | 1 |
| 200.200.76.130 | /coding/miniprj/material.html | 1 |
```

### 单测

#### 使用方法
>pytest
```
在项目根目录下执行pytest即可
```

#### 结果
>F:\Persis\SANGFOR\analyzer>pytest
```
============================= test session starts =============================
platform win32 -- Python 2.7.15, pytest-4.6.6, py-1.8.0, pluggy-0.13.0
rootdir: F:\Persis\SANGFOR\analyzer
plugins: cov-2.8.1
collected 10 items

tests\unit\log\crawler\test_crawler.py ..                                [ 20%]
tests\unit\log\record\test_record.py ....                                [ 60%]
tests\unit\log\report\test_report.py ....                                [100%]

========================== 10 passed in 0.54 seconds ==========================
```

### 单测覆盖率

#### 使用方法
>pytest --cov ./
```
在项目根目录下执行pytest --cov ./
```

#### 结果

>F:\Persis\SANGFOR\analyzer>pytest --cov ./
```
============================= test session starts =============================
platform win32 -- Python 2.7.15, pytest-4.6.6, py-1.8.0, pluggy-0.13.0
rootdir: F:\Persis\SANGFOR\analyzer
plugins: cov-2.8.1
collected 10 items

tests\unit\log\crawler\test_crawler.py ..                                [ 20%]
tests\unit\log\record\test_record.py ....                                [ 60%]
tests\unit\log\report\test_report.py ....                                [100%]

---------- coverage: platform win32, python 2.7.15-final-0 -----------
Name                                     Stmts   Miss  Cover
------------------------------------------------------------
cmd\__init__.py                              0      0   100%
cmd\cmd_parse.py                            27     27     0%
log\__init__.py                              3      0   100%
log\crawler.py                              15      0   100%
log\load.py                                 17     13    24%
log\record.py                               47      5    89%
log\report.py                               42      3    93%
main.py                                      7      7     0%
tests\__init__.py                            0      0   100%
tests\unit\__init__.py                       0      0   100%
tests\unit\cmd\__init__.py                   0      0   100%
tests\unit\log\__init__.py                   0      0   100%
tests\unit\log\crawler\__init__.py           0      0   100%
tests\unit\log\crawler\fake_data.py          4      0   100%
tests\unit\log\crawler\test_crawler.py      12      0   100%
tests\unit\log\record\__init__.py            0      0   100%
tests\unit\log\record\fake_data.py           7      0   100%
tests\unit\log\record\test_record.py        26      0   100%
tests\unit\log\report\__init__.py            0      0   100%
tests\unit\log\report\fake_data.py           6      0   100%
tests\unit\log\report\test_report.py        22      0   100%
------------------------------------------------------------
TOTAL                                      235     55    77%


========================== 10 passed in 0.61 seconds ==========================
```
