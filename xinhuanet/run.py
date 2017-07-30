#-*- coding:utf-8-*-
from scrapy import cmdline
from xinhuanet.log import log_util


if __name__ == '__main__':
    #1. 屏蔽部分运行时warning信息的输出
    import warnings
    warnings.filterwarnings("ignore")
    
    #2. 定义sys、info、error各级别日志的handler并注册
    log_util.register_handlers()
    
    #3. 启动该爬虫运行
    log_util.write_sys("启动xinhuanet爬虫运行")
    cmdline.execute('scrapy crawl xinhuanet'.split())