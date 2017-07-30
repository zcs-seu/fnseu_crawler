# -*- coding: utf-8 -*-

# Scrapy settings for xinhuanet project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
from xinhuanet.config.config import WebsiteInfo

BOT_NAME = 'xinhuanet'
BOT_VERSION = '1.0'
SPIDER_MODULES = ['xinhuanet.spiders']
NEWSPIDER_MODULE = 'xinhuanet.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

##防止被ban策略（1）禁用COOKIES
COOKIES_ENABLES=False

#data
ITEM_PIPELINES = {'xinhuanet.pipelines.MongoDBPipeline':300}

SCHEDULER = 'xinhuanet.scrapy_redis.scheduler.Scheduler'
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'xinhuanet.scrapy_redis.queue.SpiderPriorityQueue'
# SCHEDULER_QUEUE_CLASS = 'scrapyWithBloomfilter_demo.scrapy_redis.queue.SpiderSimpleQueue'

#depth
DEPTH_LIMIT=WebsiteInfo.crawler_depth

#防止被ban策略（2）设置下载延迟
DOWNLOAD_DELAY = WebsiteInfo.crawler_delay
DOWNLOAD_TIMEOUT = WebsiteInfo.crawler_timeout


#防止被ban策略（3）取消默认的useragent,使用新的轮询useragent
DOWNLOADER_MIDDLEWARES = {
   'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
   'xinhuanet.middlewares.rotate_useragent.RotateUserAgentMiddleware': 400,
   #防止被ban策略（4）轮询代理IP，由于高质量的代理IP难以获得，故此处暂时不予使用
   #'xinhuanet.middlewares.auto_ip_proxy.AutoProxyMiddleware': 543,
}


# 种子队列的信息
REDIE_URL = None
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# 去重队列的信息
FILTER_URL = None
FILTER_HOST = 'localhost'
FILTER_PORT = 6379
FILTER_DB = 0
# REDIS_QUEUE_NAME = 'OneName'   # 如果不设置或者设置为None，则使用默认的，每个spider使用不同的去重队列和种子队列。如果设置了，则不同spider共用去重队列和种子队列


LOG_LEVEL = 'INFO'
CONCURRENT_REQUESTS =WebsiteInfo.crawler_threads   # 并发