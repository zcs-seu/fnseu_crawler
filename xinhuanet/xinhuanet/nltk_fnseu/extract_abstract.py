#-*- coding:utf-8-*-
import sys
from xinhuanet.config.config import DetailRule
from xinhuanet.log import log_util
from xinhuanet.utils.exce_info import exce_parse

def parse_abstract(html,hxs,url_ctype):
    try:
        abstract_rules = DetailRule.allowed_channels[url_ctype]["abstract_rules"]
        for rule_id in abstract_rules:
            xpath = abstract_rules[rule_id]["xpath"]
            try:
                abstract_str = hxs.select(xpath).extract()[0].strip()
                if abstract_str:
                    return abstract_str
            except Exception, e:
                continue;
    except:
        log_util.write_err("摘要解析失败:"+exce_parse.get_exce_info(sys.exc_info()))
    return ""