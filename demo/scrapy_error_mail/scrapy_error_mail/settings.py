# -*- coding: utf-8 -*-
import os
from datetime import datetime

# Scrapy settings for scrapy_error_mail project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_error_mail'

SPIDER_MODULES = ['scrapy_error_mail.spiders']
NEWSPIDER_MODULE = 'scrapy_error_mail.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'scrapy_error_mail (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrapy_error_mail.middlewares.ScrapyErrorMailSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'scrapy_error_mail.middlewares.ScrapyErrorMailDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    # 'scrapy.extensions.telnet.TelnetConsole': None,
    'lzc.extensions.closespider.CloseSpider': 200,
}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'scrapy_error_mail.pipelines.ScrapyErrorMailPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

date = datetime.now()
# 日志文件设置
LOG_LEVEL = 'DEBUG'
# LOG_LEVEL = 'WARNING'
LOG_ENCODING = 'utf-8'
# 判断是否存在log文件夹，不存在则创建
if os.path.exists('./log'):
    print('Log folder already exists.Do nothing.')
else:
    print('There is no log folder for storage, create!')
    os.makedirs('log')
LOG_FILE = 'log/{}-{}-{}T{}_{}_{}.log'.format(date.year, date.month, date.day, date.hour, date.minute, date.second)

# 错误数达到该值时结束爬虫且发送邮件
CLOSESPIDER_ERRORCOUNT = 1

# 发送邮件相关设置
# 收件人
STATSMAILER_RCPTS = ['weipan@jianshutech.com', 'liuzc@jianshutech.com', 'chensy@jianshutech.com']
# STATSMAILER_RCPTS = 'liuzc@jianshutech.com,chensy@jianshutech.com,weipan@jianshutech.com'
# 项目名
PROJECT_NAME = ' 测-试 hahash '
# 邮件发送服务器
MAIL_HOST = 'smtphz.qiye.163.com'
# 发件人地址
MAIL_FROM = 'liuzc@jianshutech.com'
# 授权码或者密码
MAIL_PASS = '4faNFstCz5jMUyU7'
# 邮件发送服务器端口
MAIL_PORT = 465
