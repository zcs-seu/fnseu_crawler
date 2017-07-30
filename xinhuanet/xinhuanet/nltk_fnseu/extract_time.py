#-*- coding:utf-8-*-
import re
import sys
from xinhuanet.config.config import DetailRule, WebsiteInfo
from xinhuanet.utils.time_transfer.transfer import transfer_time
from xinhuanet.log import log_util
from xinhuanet.utils.exce_info import exce_parse

def parse_time(html,hxs,url_ctype):
    try:
        time_rules=DetailRule.allowed_channels[url_ctype]["time_rules"]
        for rule_id in time_rules:
            xpath=time_rules[rule_id]["xpath"]
            time_format=time_rules[rule_id]["temp"]
            regex=time_rules[rule_id]["regex"]
            try:
                time_strs=hxs.select(xpath).extract()
                for time_str in time_strs:
                    rem = re.search(regex, time_str)
                    if rem:
                        time_str = rem.group()
                        dest_time=transfer_time(time_str.strip(),time_format,WebsiteInfo.GMT_FORMAT)
                        if dest_time:
                            return dest_time
            except Exception,e:
                print e
                continue;
    except:
        log_util.write_err("时间解析失败:"+exce_parse.get_exce_info(sys.exc_info()))
    return ""
