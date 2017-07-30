# -*_ encoding:utf-8 _*_
#!/usr/bin/env python
'''
用于获得网页的原始编码，
取自网页自己声明的编码，
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" >
,如果网页中不存在改标签，则返回none
'''
import chardet

from bs4 import BeautifulSoup
def getCoding(html_code):
    """
    根据页面判断其编码
        （1）根据其自身指定
        （2）若其自身未指定，则需要使用chardet判断
    :param html_code:
    :return:
    """
    encoding=getEncoding(html_code)
    if encoding:
        return encoding
    else:
        return chardet.detect(html_code)
def getEncoding(html_code):
    soup = BeautifulSoup(html_code)
    tags = soup.findAll('meta')
    for tag in tags:
        if tag.has_attr('http-equiv') and tag['http-equiv'].lower() == 'content-type':
            index = tag['content'].find('=')
            if index > -1:
                return tag['content'][index + 1:]
    return None
if '__main__' ==__name__:
    import urllib
    url='http://tech.sina.com.cn/i/2014-10-14/08059691430.shtml'
    print getCoding(urllib.urlopen(url).read())
