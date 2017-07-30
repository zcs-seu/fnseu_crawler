# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    crawlerid = Field()
    url = Field()
    html_code = Field()
    encoding = Field()
    title = Field()
    authors = Field()
    content = Field()
    time = Field()
    source = Field()
    editor=Field()
    ctype = Field()
    subtype = Field()
    keywords = Field()
    abstract = Field()
    
    copyright = Field()
    originality = Field()
    type = Field() 


    def __init__(self):
        Item.__init__(self)
        #爬取下来的一个全局唯一ID
        self['crawlerid'] = ''
        #页面链接
        self['url'] = ''
        #html源码
        self['html_code'] = ''
        #页面编码
        self['encoding'] = ''
        #标题
        self['title'] = ''
        #作者
        self['authors'] = []
        #正文
        self['content'] = ''
        #新闻时间
        self['time'] = ''
        #来源
        self['source']=''
        #编辑
        self['editor']=''
        #频道类别
        self['ctype'] = ''
        #频道类别
        self['subtype'] = ''
        #关键词
        self['keywords'] = []
        #摘要
        self['abstract'] = ''
        
        self['copyright'] = ''
        self['originality'] = ''
        self['type'] = 'text'


    def __set__(self):
        return 'time:%s CrawlItem(url: %s)' % self.time % self.url
