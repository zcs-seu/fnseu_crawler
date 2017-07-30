#-*- coding:utf-8-*-
import re
import sys  
from xinhuanet.config.config import DetailRule
from xinhuanet.log import log_util
from xinhuanet.utils.exce_info import exce_parse

pattern = re.compile(u"([\u4e00-\u9fa5]+)" ) 

def parse_editor(html,hxs,url_ctype):
    try:
        editor_rules = DetailRule.allowed_channels[url_ctype]["editor_rules"]
        for rule_id in editor_rules:
            xpath = editor_rules[rule_id]["xpath"]
            prefix = editor_rules[rule_id]["prefix"]
            try:
                for cur_str in hxs.select(xpath.decode("utf8")).extract():
                    cur_str=cur_str.replace("\s","")
                    editor_str = cur_str.strip().partition(prefix)[2]
                    if editor_str:
                        res=[]
                        results =  pattern.findall(editor_str)  
                        for result in results:  
                            res.append([result])
                        return res
            except Exception, e:
                print e
                continue;
    except:
        log_util.write_err("编辑解析失败:"+exce_parse.get_exce_info(sys.exc_info()))
    return []