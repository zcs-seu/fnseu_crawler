#!usr/local/bin/python
# -*-coding:utf-8 -*-
"""

    新闻类、论坛类、政府网站类网页正文识别的底层实现文件
    
    描述：
        调用开源的正文抽取工具goose，实现新闻类、论坛类、政府网站类
        网页的正文抽取
            
"""
from goose import Goose
from goose.text import StopWordsChinese
g = Goose({'stopwords_class': StopWordsChinese}) 
def get_content_by_html(html):
    """
        调用开源的正文抽取工具goose，实现新闻类、论坛类、政府网站类
            网页的正文抽取的工具函数
        :param html:待解析网页源码
        :returns:str— —网页中的正文信息
    """
    article = g.extract(raw_html=html)
    content = article.cleaned_text
    return content;

def get_title_by_html(html):
    """
        调用开源的正文抽取工具goose，实现新闻类、论坛类、政府网站类
            网页的标题抽取的工具函数
        :param html:待解析网页源码
        :returns:str— —网页中的标题信息
    """
    article = g.extract(raw_html=html)
    title = article.title
    return title;


