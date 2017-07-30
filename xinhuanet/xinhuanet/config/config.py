#-*- coding:utf-8-*-
#!/usr/bin/env python
#program:
#      analyze the configure.xml and get argments
#      本文件中所有中文均为unicode编码
#2014/09/23 zhiwei_yuan first release
import os
import sys
import inspect
from bs4 import BeautifulSoup
from xinhuanet.log import log_util
from xinhuanet.utils.time_transfer.transfer import transfer_time
from xinhuanet.utils.exce_info import exce_parse

#获得本文件所处路径
this_file = inspect.getfile(inspect.currentframe())
path = os.path.abspath(os.path.dirname(this_file))

#读取配置文件configure.xml
try:
    log_util.write_sys("读取并解析配置文件configure.xml开始")
    txt=open(path+os.sep+"configure.xml").read()
    soup=BeautifulSoup(txt,"lxml")
    log_util.write_sys("读取并解析配置文件configure.xml结束")
except:
    log_util.write_err("配置文件configure.xml不存在、或者解析出错:"+\
    exce_parse.get_exce_info(sys.exc_info()))
    exit(0)

class mongodb:
    host=soup.xml.configuration.dbs.mongodb.host.string
    port=soup.xml.configuration.dbs.mongodb.port.string
    database=soup.xml.configuration.dbs.mongodb.database.string
    table=soup.xml.configuration.dbs.mongodb.table.string
    gridfsdb=soup.xml.configuration.dbs.mongodb.gridfsdb.string
class mysql:
    host=soup.xml.configuration.dbs.mysql.host.string
    port=soup.xml.configuration.dbs.mysql.port.string
    user=soup.xml.configuration.dbs.mysql.user.string
    database=soup.xml.configuration.dbs.mysql.database.string
    passwd=soup.xml.configuration.dbs.mysql.passwd.string
    charset=soup.xml.configuration.dbs.mysql.charset.string
    ucltable=soup.xml.configuration.dbs.mysql.ucltable.string
    filetable=soup.xml.configuration.dbs.mysql.filetable.string
class redis:
    host=soup.xml.configuration.dbs.redis.host.string
    port=soup.xml.configuration.dbs.redis.port.string
    db=soup.xml.configuration.dbs.redis.db.string
    dupdatabase=soup.xml.configuration.dbs.redis.dupdatabase.string
    src=soup.xml.configuration.dbs.redis.src.string
    rs=soup.xml.configuration.dbs.redis.rs.string
    ans=soup.xml.configuration.dbs.redis.ans.string
    src_test=soup.xml.configuration.dbs.redis.src_test.string
    rs_test=soup.xml.configuration.dbs.redis.rs_test.string
class WebsiteInfo:
    crawler_name=soup.xml.crawler_name.string
    crawler_id=soup.xml.crawler_id.string
    crawler_depth=int(soup.xml.crawler_depth.string)
    crawler_delay=int(soup.xml.crawler_delay.string)
    crawler_timeout = int(soup.xml.crawler_timeout.string)
    crawler_threads = int(soup.xml.crawler_threads.string)
    GMT_FORMAT=soup.xml.gmt_format.string
    start_urls=[]
    allowed_domains=[]

    for start_url in soup.xml.configuration.urls.start_urls.find_all("start_url"):
        start_urls.append(start_url.string)
    for domain in soup.xml.configuration.urls.allowed_domains.find_all("domain"):
        allowed_domains.append(domain.string)
class DetailRule:
    url_depth=0
    has_date=False


    allowed_channels = {}
    dest_dateformat="%Y-%m-%d"
    date_rules={}

    detail_rules=soup.xml.configuration.parse_rules.detail_rules;

    url_depth=int (detail_rules.url_depth.string)
    has_date=bool(detail_rules.has_date.string)

    date_rules["used"]=bool(detail_rules.date.used.string)
    date_rules["dest_format"] = detail_rules.date.dest_format.string

    for date_rule in detail_rules.date.find_all("rule"):
        date_rules[date_rule.rule_id.string] = {}
        date_rules[date_rule.rule_id.string]['regex'] = date_rule.regex.string
        date_rules[date_rule.rule_id.string]['format'] = date_rule.format.string


    for channel in detail_rules.allowed_channels.find_all("channel"):
        cur_channel_rules={}

        cur_channel_rules["ctype"]=channel.attrs["ctype"]
        
        #解析关键词规则
        cur_keywords_rules={}
        rule_list = detail_rules.public_rules.keywords_rules.find_all("rule")
        rule_list.extend(channel.keywords_rules.find_all("rule"))
        for keywords_rule in rule_list:
            cur_keywords_rules[keywords_rule.rule_id.string]={}
            cur_keywords_rules[keywords_rule.rule_id.string]['xpath']=keywords_rule.xpath.string
            cur_keywords_rules[keywords_rule.rule_id.string]['sep'] = keywords_rule.sep.string
        cur_channel_rules["keywords_rules"]=cur_keywords_rules
        
        #解析摘要规则
        cur_abstract_rules={}
        rule_list = detail_rules.public_rules.abstract_rules.find_all("rule")
        rule_list.extend(channel.abstract_rules.find_all("rule"))
        for abstract_rule in rule_list:
            cur_abstract_rules[abstract_rule.rule_id.string]={}
            cur_abstract_rules[abstract_rule.rule_id.string]['xpath']=abstract_rule.xpath.string
        cur_channel_rules["abstract_rules"]=cur_abstract_rules
        
        #解析编辑规则
        cur_editor_rules={}
        rule_list = detail_rules.public_rules.editor_rules.find_all("rule")
        rule_list.extend(channel.editor_rules.find_all("rule"))
        for editor_rule in rule_list:
            cur_editor_rules[editor_rule.rule_id.string]={}
            cur_editor_rules[editor_rule.rule_id.string]['xpath']=editor_rule.xpath.string
            print editor_rule.xpath.string
            cur_editor_rules[editor_rule.rule_id.string]['prefix'] = editor_rule.pprefix.string
        cur_channel_rules["editor_rules"]=cur_editor_rules

        #解析标题规则
        cur_title_rules={}
        rule_list = detail_rules.public_rules.title_rules.find_all("rule")
        rule_list.extend(channel.title_rules.find_all("rule"))
        for title_rule in rule_list:
            cur_title_rules[title_rule.rule_id.string]={}
            cur_title_rules[title_rule.rule_id.string]['xpath']=title_rule.xpath.string
            cur_title_rules[title_rule.rule_id.string]['sep'] = title_rule.sep.string
        cur_channel_rules["title_rules"]=cur_title_rules


        #解析时间规则
        cur_time_rules={}
        rule_list=detail_rules.public_rules.time_rules.find_all("rule")
        rule_list.extend(channel.time_rules.find_all("rule"))
        for time_rule in rule_list:
            cur_time_rules[time_rule.rule_id.string]={}
            cur_time_rules[time_rule.rule_id.string]['xpath']=time_rule.xpath.string
            cur_time_rules[time_rule.rule_id.string]['temp'] = time_rule.temp.string
            cur_time_rules[time_rule.rule_id.string]['regex'] = time_rule.regex.string
        cur_channel_rules["time_rules"]=cur_time_rules

        # 解析来源规则
        cur_source_rules = {}
        rule_list = detail_rules.public_rules.source_rules.find_all("rule")
        rule_list.extend(channel.source_rules.find_all("rule"))
        for source_rule in rule_list:
            cur_source_rules[source_rule.rule_id.string] = {}
            cur_source_rules[source_rule.rule_id.string]['xpath'] = source_rule.xpath.string
        cur_channel_rules["source_rules"] = cur_source_rules

        allowed_channels[channel.attrs["name"]]=cur_channel_rules




if __name__ == "__main__":
    soup=BeautifulSoup(open("configure.xml").read(),"lxml")
    print mongodb.host
    print mongodb.port
    print mongodb.database
    print mongodb.table
    print mysql.host
    print mysql.port
    print mysql.user
    print mysql.passwd
    print mysql.database
    print mysql.filetable
    print mysql.charset
    print redis.host
    print redis.port
    print redis.db
    print redis.dupdatabase
    print redis.src
    print redis.rs
    print redis.ans
    print WebsiteInfo.crawler_name
    print WebsiteInfo.start_urls
    print WebsiteInfo.allowed_domains
    print transfer_time(u"2017年07月01日 17:53:27",DetailRule.allowed_channels["mil"]\
                        ["time_rules"]["pub_1"]["temp"],"%a, %d %b %Y %H:%M:%S GMT")