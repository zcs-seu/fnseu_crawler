#-*- coding:utf-8-*-
from bs4 import BeautifulSoup

def get_bs_by_html(html):
    """
        使用启发式方法，自动确定其Beautifulsoup使用的解析器，并生成对应的DOM树
        :param html:网页源码
        :returns:tag— —Beautifulsoup对象节点
    """
    if not html:return None
    pre_length = len(html);
    bs1 = BeautifulSoup(html, "lxml");
    cur_length1 = len(str(bs1));
    if float(cur_length1) / float(pre_length) >= 0.8:
        return bs1;
    bs2 = BeautifulSoup(html, "html.parser");
    cur_length2 = len(str(bs2));
    if float(cur_length2) / float(pre_length) >= 0.8:
        return bs2;
    if cur_length1 >= cur_length2:
        return bs1;
    else:
        return bs2;