# -*- coding: utf-8 -*-
# @Author: 刘兆承
# @Time  :2019/7/24 10:56
import os
from scrapy import cmdline

# os.system('scrapy crawl test')
cmdline.execute('scrapy crawl test'.split())
