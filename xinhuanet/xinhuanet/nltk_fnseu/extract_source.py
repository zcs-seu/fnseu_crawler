#-*- coding:utf-8-*-
import sys
from xinhuanet.log import log_util
from xinhuanet.utils.exce_info import exce_parse
from xinhuanet.config.config import DetailRule


def parse_source(html,hxs,url_ctype):
    try:
        source_rules=DetailRule.allowed_channels[url_ctype]["source_rules"]
        for rule_id in source_rules:
            xpath=source_rules[rule_id]["xpath"]
            try:
                source_str=hxs.select(xpath).extract()[0].strip()
                if source_str:
                    source_str = source_str.rpartition(u"来源：")[2]
                    source_str = source_str.rpartition(u"来源:")[2]
                    return source_str
            except Exception,e:
                continue;
    except:
        log_util.write_err("来源解析失败:"+exce_parse.get_exce_info(sys.exc_info()))
    return ""