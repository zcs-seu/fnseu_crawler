# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import redis
from pymongo import MongoClient
from xinhuanet.config import config
from xinhuanet.log import log_util
from xinhuanet.utils.exce_info import exce_parse


class MongoDBPipeline(object):
    def __init__(self):
        log_util.write_sys('=====================init mongodb=========================')
        log_util.write_sys('init mongodb start')
        try:
            con = MongoClient(host=config.mongodb.host,port=int(config.mongodb.port))
            exec ("db = con." + config.mongodb.database)
            exec ("self.dbpool = db." + config.mongodb.table)
        except:
            log_util.write_err("MongoDB连接失败，请检查相关配置:"+exce_parse.get_exce_info(sys.exc_info()))
        log_util.write_sys('init mongodb end')

    def process_item(self, item, spider):
        print '$$$$intsert into mongodb %s start$$$$' % (item['url'])
        log_util.write_info('$$$$intsert into mongodb %s start$$$$' % (item['url']))
        ucl = {
                "url" : item['url'],
                "html_code" : item['html_code'],
                "encoding" : item['encoding'],
                "time" : item['time'],
                "type" : item['type'],
                "title" : item['title'],
                "authors" : item['authors'],
                "editor" : item['editor'],
                "content" : item['content'],
                "copyright" : item['copyright'],
                "source" : item['source'],
                "originality" : item['originality'],
                "abstract" : item['abstract'],
                "ctype" : item['ctype'],
                "subtype" : item['subtype'],
                "keywords" : item['keywords']
            }
        try:
            self.dbpool.insert(ucl)  # 插入mongodb
            log_util.write_info('$$$$insert into mongodb success$$$$')
        except Exception, e:
            log_util.write_info('$$$$insert into mongodb fail$$$$')
            print '$$$$insert into mongodb fail$$$$'
