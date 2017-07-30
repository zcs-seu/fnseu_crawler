#-*- coding:utf-8-*-
import chardet
import time

import sys
import redis
import scrapy
from scrapy import Selector
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

from xinhuanet.config import config
from xinhuanet.config.config import WebsiteInfo
from xinhuanet.items import DemoItem
from xinhuanet.nltk_fnseu.html_parse import parse_page
from xinhuanet.utils.distinguish.pageType_dist import is_detail
from xinhuanet.utils.encoding_detect import Encoding
from xinhuanet.utils.url_parse.parse_url import filter_invalid_urls
from xinhuanet.log import log_util
from xinhuanet.utils.exce_info import exce_parse



class DemoSpider(scrapy.Spider):

    """
    读取配置文件中的爬虫名、ID、起始链接、允许的域名
    """
    # Spider名，用于启动scrapy工程
    name = WebsiteInfo.crawler_name
    allowed_domains = WebsiteInfo.allowed_domains

    start_urls = WebsiteInfo.start_urls
    # 爬虫ID
    crawlerid = WebsiteInfo.crawler_id

    # URL解析后调用的callback，response包含了抓到的网页的内容
    # parse可以返回Request列表，或者items列表，如果返回的是Request，
    # 则这个Request会放到下一次需要抓取的队列，如果返回items，
    # 则对应的items才能传到pipelines处理
    def parse(self, response):
        log_util.write_info("$$$$开始解析：" + response.url.encode("utf-8")+"$$$$")
        print "$$$$开始解析：" + response.url.encode("utf-8")+"$$$$"
        # 利用scrapy自带的html源码解析器进行解析
        hxs = Selector(response)

        #记录原链接
        respurl = response.url.encode('UTF-8')

        #判断是否为信息页
        ctype,url_ctype= is_detail(respurl)
        if ctype:  # 确定为信息页
            log_util.write_info("$$$$详情页：" + respurl + "$$$$")
            print "$$$$详情页：" + respurl + "$$$$"
            yield self.parse_page(response, ctype ,url_ctype)
        print "$$$$列表页：" + respurl + "$$$$"
        
        #确定为列表页
        # 抽取URL
        urls = hxs.xpath('//a/@href').extract()  # 匹配得到的URL集合
        #过滤无效链接
        valid_urls=filter_invalid_urls(urls,respurl)

        # 保存链接信息
        for url in valid_urls:
            yield Request(url,callback=self.parse)



    def parse_page(self, response, ctype ,url_ctype):
        log_util.write_info("$$$$详情页解析开始：" + response.url.encode("utf-8") + "$$$$")
        print "$$$$详情页解析开始：" + response.url.encode("utf-8") + "$$$$"
        item = DemoItem()  # 采集对象的容器
        item['crawlerid'] = self.crawlerid

        item['url'] = response.url.encode('UTF-8')

        html_code=response.body;
        hxs = HtmlXPathSelector(response)

        # 此处使用了chardet检测网页编码，使用原因是因为虽然部分新浪网页在html声明中指出是使用了gb2312编码，但是实际上并不一定是
        try:
            encoding = Encoding.getCoding(html_code)
            item['html_code'] = html_code.decode(encoding, 'ignore')
            item['encoding'] = encoding
        except:
            log_util.write_err("编码识别出错:"+exce_parse.get_exce_info(sys.exc_info()))
        
        # 语义解析处理begin
        item['ctype']=ctype
        item['subtype']=url_ctype.split('/')[1]
        try:
            parse_page(item,hxs,url_ctype)
        except:
            log_util.write_err("语义解析处理出错:"+exce_parse.get_exce_info(sys.exc_info()))
        # 语义解析处理end

        # 设置爬取时间
        crawl_time = time.strftime(WebsiteInfo.GMT_FORMAT, time.localtime())

        # 如果时间信息未抽取到，将其设置为抓取时间
        if not item["time"]:
            item["time"] = crawl_time

        log_util.write_info("$$$$详情页解析结束：" + item['url'] + "$$$$")
        print "$$$$详情页解析结束：" + item['url'] + "$$$$"

        return item