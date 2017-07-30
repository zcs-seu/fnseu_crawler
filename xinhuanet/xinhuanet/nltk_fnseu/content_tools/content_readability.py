#!usr/local/bin/python
# -*-coding:utf-8 -*-
"""

    新闻类、论坛类、政府网站类网页正文识别的底层实现文件
    
    描述：
        调用开源的正文抽取工具readability，实现新闻类、论坛类、政府网站类
        网页的正文抽取
            
"""
import HTMLParser
from readability.readability import Document

def get_content_by_html(html):
    """
        调用开源的正文抽取工具goose，实现新闻类、论坛类、政府网站类
            网页的正文抽取的工具函数
        :param html:待解析网页源码
        :returns:str— —网页中的正文信息
    """
    readable_article = Document(html).summary()
    html_parser = HTMLParser.HTMLParser()
    readable_article = html_parser.unescape(readable_article)
    return readable_article


def get_title_by_html(html):
    """
        调用开源的正文抽取工具goose，实现新闻类、论坛类、政府网站类
            网页的标题抽取的工具函数
        :param html:待解析网页源码
        :returns:str— —网页中的标题信息
    """
    readable_title = Document(html).short_title()
    return readable_title