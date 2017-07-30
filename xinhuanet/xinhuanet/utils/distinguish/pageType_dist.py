#-*- coding:utf-8-*-
import re

from xinhuanet.config.config import DetailRule
from xinhuanet.utils.time_transfer.transfer import transfer_time


def is_detail(respurl):
    """
    判断网页是否为详情页
    经过调研分析可知，信息页应该具备以下条件
    :param respurl:
    :return:
    """
    urlinfo = respurl.split('/')
    length = len(urlinfo)

    if length > DetailRule.url_depth:
        rem= has_date(respurl)
        print "匹配时间信息",rem
        if rem:
            print "匹配时间信息成功"
            #ctype为调整后的类别，url_ctype为其实际类别
            ctype,url_ctype = Klass(respurl)
            if ctype:
                return ctype,url_ctype
            else:
                print "info:" + respurl + " 1not parse"
        else:
            print "info:" + respurl + " not 2parse"
    else:
        print "info:" + respurl + " not 3parse"
    return None,None


def has_date(respurl):
    """
    判断url中是否含有预期的时间要素
    :param respurl:
    :return:
    """
    date_rules=DetailRule.date_rules
    if not date_rules["used"]:
        return True
    for rule_id in date_rules:
        if rule_id.find("date")==-1:
            continue
        rem = re.search(date_rules[rule_id]['regex'], respurl)
        if rem:
            datestring = str(rem.group())[1:-1]
            date=transfer_time(datestring,date_rules[rule_id]['format'],date_rules["dest_format"])
            if date:
                return True
    return False


def Klass(url):
    """
    判断URL所属的频道
    :param url:
    :return:
    """
    allowed_channels=DetailRule.allowed_channels
    for channel in allowed_channels:
        if re.search(channel,url):
            return allowed_channels[channel]["ctype"],channel

    return None,None  # 其他所有的全部返回None

if __name__=="__main__":
    print is_detail("http://news.sina.com/politics/2017-06/24/c_1121203916.htm")