# scrapy_mail

## 功能
重写了 scrapy 本身自带的拓展 `scrapy.extensions.closespider.CloseSpider`  
将其从发生指定个错误时单纯停止爬虫  
变更为发生指定个错误时停止爬虫且发送错误邮件（可将日志文件作为附件）  
此处错误指的是爬虫错误（如下载图片时，图片链接返回`200`但实际上网页显示无图片时报错不在此列）  
邮件内容包含此时爬虫状态，如
```text
[ spider ] stats

start_time                                         : 2019-07-xx xxxxxx
scheduler/enqueued/memory                          : 144062
scheduler/enqueued                                 : 144062
scheduler/dequeued/memory                          : 144062
scheduler/dequeued                                 : 144062
downloader/request_count                           : 144062
downloader/request_method_count/GET                : 144062
downloader/request_bytes                           : 47828584
downloader/response_count                          : 144062
downloader/response_status_count/200               : 144062
downloader/response_bytes                          : 458870922
response_received_count                            : 144062
item_scraped_count                                 : 144062
finish_time                                        : 2019-07-xx xxxxxx
finish_reason                                      : finished

```
```text
[ spider ] stats

log_count/INFO                                     : 9
start_time                                         : 2019-07-xx xxxxxx
memusage/startup                                   : 53481472
memusage/max                                       : 53481472
scheduler/enqueued/memory                          : 3
scheduler/enqueued                                 : 3
scheduler/dequeued/memory                          : 3
scheduler/dequeued                                 : 3
downloader/request_count                           : 3
downloader/request_method_count/GET                : 3
downloader/request_bytes                           : 674
downloader/response_count                          : 3
downloader/response_status_count/200               : 3
downloader/response_bytes                          : 157937
log_count/DEBUG                                    : 3
response_received_count                            : 3
log_count/ERROR                                    : 3
spider_exceptions/IndexError                       : 3
finish_time                                        : 2019-07-xx xxxxxx
finish_reason                                      : closespider_errorcount

```

## 使用背景
1. 请将 'lzc' 文件夹复制至 scrapy 同级目录
2. `pip install maida` （需安装maida库）

## settings.py 需要设置的参数
### 1. 必要参数

```python
EXTENSIONS = {
    'lzc.extensions.closespider.CloseSpider': 200,
}

# 错误数达到该值时结束爬虫且发送邮件
CLOSESPIDER_ERRORCOUNT = 1

# 发送邮件相关设置
# 收件人
STATSMAILER_RCPTS = ['xxx@xxx.com', 'xxx@xxx.com', 'xxx@xxx.com']
# 项目名
PROJECT_NAME = ' 测-试  '
# 邮件发送服务器
MAIL_HOST = 'xxx@xxx.com'
# 发件人地址
MAIL_FROM = 'xxx@xxx.com'
# 授权码或者密码
MAIL_PASS = 'xxxxxxx'
# 邮件发送服务器端口
MAIL_PORT = 465
```

### 2. 可选参数（是否将日志文件作为附件发送）
#### Tips
当含有日志文件时，将日志文件作为附件发送，此时日志文件建议设置为 'WARNING' 及以上，避免发送过大日志文件
```python
import os
from datetime import datetime

date = datetime.now()
# 日志文件设置
# LOG_LEVEL = 'DEBUG'
LOG_LEVEL = 'WARNING'
LOG_ENCODING = 'utf-8'
# 判断是否存在log文件夹，不存在则创建
if os.path.exists('./log'):
    print('Log folder already exists.Do nothing.')
else:
    print('There is no log folder for storage, create!')
    os.makedirs('log')
LOG_FILE = 'log/{}-{}-{}T{}_{}_{}.log'.format(date.year, date.month, date.day, date.hour, date.minute, date.second)
```

## demo
[demo](https://github.com/LZC6244/scrapy_mail/tree/master/demo) 传送门
