#-*- coding:utf-8-*-
from xinhuanet.nltk_fnseu.extract_content import parse_content
from xinhuanet.nltk_fnseu.extract_source import parse_source
from xinhuanet.nltk_fnseu.extract_time import parse_time
from xinhuanet.nltk_fnseu.extract_title import parse_title
from xinhuanet.nltk_fnseu.extract_keywords import parse_keywords
from xinhuanet.nltk_fnseu.extract_abstract import parse_abstract
from xinhuanet.nltk_fnseu.extract_keywords import parse_keywords_textrank
from xinhuanet.nltk_fnseu.extract_keywords import parse_abstract_textrank
from xinhuanet.nltk_fnseu.extract_editor import parse_editor
from xinhuanet.nltk_fnseu.extract_author import parse_author


def parse_page(item,hxs,url_ctype):
    html=item["html_code"];
    
    #解析关键词
    keywords=parse_keywords(html, hxs, url_ctype)
    item["keywords"] = keywords
    #解析摘要
    abstract=parse_abstract(html, hxs, url_ctype)
    item["abstract"] = abstract
    #解析标题
    title = parse_title(html, hxs, url_ctype)
    item["title"] = title
    #解析时间
    time = parse_time(html, hxs, url_ctype)
    item["time"]=time
    #解析正文
    content = parse_content(html, hxs, url_ctype)
    item["content"] = content
    #解析来源
    source = parse_source(html, hxs, url_ctype)
    item["source"] = source
    item["copyright"] = source
    #解析编辑
    editor = parse_editor(html, hxs, url_ctype)
    item["editor"] = editor
    #解析作者
    if content:
        authors = parse_author(content)
        item["authors"] = authors
    
    #利用TextRank4ZH对未抽取到的关键词和摘要进行补偿
    if not keywords and content:
        keywords = parse_keywords_textrank(content)
        item["keywords"] = keywords
    if not keywords and title:
        keywords = parse_keywords_textrank(title)
        item["keywords"] = keywords
    if not abstract and content:
        abstract = parse_abstract_textrank(content)
        item["abstract"] = abstract
    if not abstract and title:
        item["abstract"] = title