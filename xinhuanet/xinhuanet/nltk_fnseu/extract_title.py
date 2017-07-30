#-*- coding:utf-8-*-
import sys
from xinhuanet.config.config import DetailRule
from xinhuanet.log import log_util
from xinhuanet.utils.exce_info import exce_parse

def parse_title(html,hxs,url_ctype):
    
    try:
        title_rules = DetailRule.allowed_channels[url_ctype]["title_rules"]
        for rule_id in title_rules:
            xpath = title_rules[rule_id]["xpath"]
            title_seps = title_rules[rule_id]["sep"].split(" ")
            try:
                time_str = hxs.select(xpath).extract()[0].strip()
                for title_sep in title_seps:
                    time_str=time_str.partition(title_sep)[0]
                return time_str
            except Exception, e:
                continue;
    except:
        log_util.write_err("标题解析失败:"+exce_parse.get_exce_info(sys.exc_info()))
    return ""