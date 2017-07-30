#!usr/local/bin/python
# -*-coding:utf-8 -*-
"""

    新闻类、论坛类、政府网站类网页正文识别的底层实现文件
    
    描述：
        调用开源的正文抽取工具boilerpipe，实现新闻类、论坛类、政府网站类
        网页的正文抽取
            
"""
from boilerpipe.extract import Extractor

def get_content_by_url(url):
    """
        调用开源的正文抽取工具boilerpipe，实现新闻类、论坛类、政府网站类
            网页的正文抽取的工具函数（不推荐、编码识别有时出问题）
        :param url:待解析网页链接
        :returns:str— —网页中的正文信息
    """
    extractor = Extractor(extractor='ArticleExtractor', url=url);
    processed_plaintext = extractor.getText();
    return processed_plaintext;
def get_contenthtml_by_url(url):
    """
        调用开源的正文抽取工具boilerpipe，实现新闻类、论坛类、政府网站类
            网页的正文抽取的工具函数（不推荐、编码识别有时出问题）
        :param url:待解析网页链接
        :returns:str— —正文信息得到突出的网页源码
    """
    extractor = Extractor(extractor='ArticleExtractor', url=url);
    highlighted_html = extractor.getHTML()
    return highlighted_html;
def get_content_by_html(html):
    """
        调用开源的正文抽取工具boilerpipe，实现新闻类、论坛类、政府网站类
            网页的正文抽取的工具函数（推荐）
        :param url:待解析网页源码
        :returns:str— —网页中的正文信息
    """
    extractor = Extractor(extractor='ArticleExtractor', html=html)
    processed_plaintext = extractor.getText();
    return processed_plaintext;
def get_contenthtml_by_html(html):
    """
        调用开源的正文抽取工具boilerpipe，实现新闻类、论坛类、政府网站类
            网页的正文抽取的工具函数（推荐）
        :param url:待解析网页源码
        :returns:str— —正文信息得到突出的网页源码
    """
    extractor = Extractor(extractor='ArticleExtractor', html=html)
    highlighted_html = extractor.getHTML()
    return highlighted_html;