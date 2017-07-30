﻿#-*- coding:utf-8-*-
import re
import nltk
import jieba
import sys
from xinhuanet.log import log_util
from xinhuanet.utils.exce_info import exce_parse

pattern_1 = re.compile(ur"记者\s{0,4}([\u4e00-\u9fa5、\s\u3000]+)\s{0,4}报道")
pattern_2 = re.compile(ur"[(（]记者\s{0,4}([\u4e00-\u9fa5、\s\u3000]+)\s{0,4}[)）]")
pattern_3 = re.compile(ur"记者\s{0,4}([\u4e00-\u9fa5、\s\u3000]+)\s{0,4}摄") 
pattern_4 = re.compile(ur"[(（]([\u4e00-\u9fa5、\s\u3000]+)[）)]")

def parse_author_public(content):
    try:
        #（1）记者 xxx报道
        results =  pattern_1.findall(content)  
        for result in results:
            result=result.strip()
            result=result.replace(u"\u3000",u" ")
            result=result.replace(u"、",u" ")
            if result:
                if result.find(u" ")!=-1:
                    return result.split(u" ")
                return [result]
        #（2）（记者 xxx）
        results =  pattern_2.findall(content)  
        for result in results:
            result=result.strip()
            result=result.replace(u"\u3000",u" ")
            result=result.replace(u"、",u" ")
            if result:
                if result.find(u" ")!=-1:
                    return result.split(u" ")
                return [result]
        #（3）记者 xxx摄
        results =  pattern_3.findall(content)  
        for result in results:
            result=result.strip()
            result=result.replace(u"\u3000",u" ")
            result=result.replace(u"、",u" ")
            if result:
                if result.find(u" ")!=-1:
                    return result.split(u" ")
                return [result]
        #（4）（xxx、xxx）
        cur_list = content.split(u"。")
        first = cur_list[0]
        second = cur_list[len(cur_list)-1]
        results =  pattern_4.findall(first)  
        for result in results:
            result=result.strip()
            result=result.replace(u"\u3000",u" ")
            result=result.replace(u"、",u" ")
            if result:
                if result.find(u" ")!=-1:
                    return result.split(u" ")
                if len(result)>1 and len(result)<4:
                    return [result]
        results =  pattern_4.findall(second)  
        for result in results:
            result=result.strip()
            result=result.replace(u"\u3000",u" ")
            result=result.replace(u"、",u" ")
            if result:
                if result.find(u" ")!=-1:
                    return result.split(u" ")
                if len(result)>1 and len(result)<4:
                    return [result]
    except:
        log_util.write_err("作者解析失败:"+exce_parse.get_exce_info(sys.exc_info()))
    return []
def parse_author(content):
    authors = parse_author_public(content)
    
    authors=filter(lambda x:len(x)>1 and len(x)<4, authors)
    res=[]
    map(lambda x:res.append([x]),authors)
    return res

    
 
if __name__=="__main__":
    content=u"记者 吴新伟 报道"
    content=u"(记者 吴新伟)"
    content=u"记者 吴新伟摄"
    content=u"（见习记者曹菲于婷 　实习生江珊鞠菊摄影报道）"
    #content=u"（记者 邢婷 王晨）"
    print parse_author(content)