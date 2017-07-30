#!usr/local/bin/python
# -*-coding:utf-8 -*-
"""

    新闻、政府网站类网页正文识别底层工具函数实现文件
    
    描述：
        主要实现新闻类、论坛类、政府网站类网页的正文抽取
            
"""
import re
import os
import sys
import inspect
this_file = inspect.getfile(inspect.currentframe())
path = os.path.abspath(os.path.dirname(this_file))
path = path.rpartition("/")[0];
path = path.rpartition("/")[0];
if path not in sys.path:
    sys.path.append(path)


def remove_copyright(content):
    """
        去除正文中的版权信息
        :param content:抽取到的正文信息(字符串形式)
        :returns:str— —返回过滤版权信息后的网页中的正文信息，若未找到则返回None
    """
    rules=[re.compile(u"\u7248\u6743\u58f0\u660e[:：].*\r?\n"),\
           re.compile(u"\u7248\u6743\u7533\u660e[:：].*\r?\n"),\
           re.compile(u"\u514d\u8d23\u58f0\u660e[:：].*\r?\n"),\
           re.compile(u"\u514d\u8d23\u7533\u660e[:：].*\r?\n"),\
           re.compile(u"\u7248\u6743\u58f0\u660e[ \t]+[:：].*\r?\n"),\
           re.compile(u"\u7248\u6743\u7533\u660e[ \t]+[:：].*\r?\n"),\
           re.compile(u"\u514d\u8d23\u58f0\u660e[ \t]+[:：].*\r?\n"),\
           re.compile(u"\u514d\u8d23\u7533\u660e[ \t]+[:：].*\r?\n"),\
           re.compile(u"\u7248\u6743\u58f0\u660e[:：][ \t]+.*\r?\n"),\
           re.compile(u"\u7248\u6743\u7533\u660e[:：][ \t]+.*\r?\n"),\
           re.compile(u"\u514d\u8d23\u58f0\u660e[:：][ \t]+.*\r?\n"),\
           re.compile(u"\u514d\u8d23\u7533\u660e[:：][ \t]+.*\r?\n"),\
           re.compile(u"\u7248\u6743\u58f0\u660e[ \t]+[:：][ \t]+.*\r?\n"),\
           re.compile(u"\u7248\u6743\u7533\u660e[ \t]+[:：][ \t]+.*\r?\n"),\
           re.compile(u"\u514d\u8d23\u58f0\u660e[ \t]+[:：][ \t]+.*\r?\n"),\
           re.compile(u"\u514d\u8d23\u7533\u660e[ \t]+[:：][ \t]+.*\r?\n"),\
           re.compile(u"\u7248\u6743\u58f0\u660e[:：].*[。！？]"),\
           re.compile(u"\u7248\u6743\u7533\u660e[:：].*[。！？]"),\
           re.compile(u"\u514d\u8d23\u58f0\u660e[:：].*[。！？]"),\
           re.compile(u"\u514d\u8d23\u7533\u660e[:：].*[。！？]"),\
           re.compile(u"\u7248\u6743\u58f0\u660e[ \t]+[:：].*[。！？]"),\
           re.compile(u"\u7248\u6743\u7533\u660e[ \t]+[:：].*[。！？]"),\
           re.compile(u"\u514d\u8d23\u58f0\u660e[ \t]+[:：].*[。！？]"),\
           re.compile(u"\u514d\u8d23\u7533\u660e[ \t]+[:：].*[。！？]"),\
           re.compile(u"\u7248\u6743\u58f0\u660e[:：][ \t]+.*[。！？]"),\
           re.compile(u"\u7248\u6743\u7533\u660e[:：][ \t]+.*[。！？]"),\
           re.compile(u"\u514d\u8d23\u58f0\u660e[:：][ \t]+.*[。！？]"),\
           re.compile(u"\u514d\u8d23\u7533\u660e[:：][ \t]+.*[。！？]"),\
           re.compile(u"\u7248\u6743\u58f0\u660e[ \t]+[:：][ \t]+.*[。！？]"),\
           re.compile(u"\u7248\u6743\u7533\u660e[ \t]+[:：][ \t]+.*[。！？]"),\
           re.compile(u"\u514d\u8d23\u58f0\u660e[ \t]+[:：][ \t]+.*[。！？]"),\
           re.compile(u"\u514d\u8d23\u7533\u660e[ \t]+[:：][ \t]+.*[。！？]"),\
        ]
    
    for rule in rules:
        content=re.sub(rule,"",content)
    return content.strip()


def content_format(content):
    """
        去除正文中的连续换行
        :param content:抽取到的正文信息(字符串形式)
        :returns:str— —返回规格化后的网页中的正文信息，若未找到则返回None
    """
    
    if not content:
        return "",0,0,0,0,0
    
    #去除空格
    lines=content.split("\n")
    r0=re.compile(r"[ \t]+")
    lines=map(lambda line:re.sub(r0,"",line),lines)
    lines=filter(lambda line:line.strip()!="",lines)
    content="\n".join(lines)
    #去除正文中的连续换行
    
    r=re.compile(r"(\r*\n)+")
    content=re.sub(r,"\n",content)
    
    #去除版权声明等
    content=remove_copyright(content)

    #获得正文字数
    wordLen=len(content)
    
    #获得正文段数
    paraNum=len(content.split("\n"))
    if paraNum==0:paraNum=0.00000000001

    #获得标点数
    cn_segs=[u"，",u"。",u"！",u"？",u"：",u"；",u"、"]
    segs=[",",".","!","?",":",";"]
    cn_segs_num=0;
    for cn_seg in cn_segs:
        cn_segs_num+=content.count(cn_seg)
    segs_num=0;
    for seg in segs:
        segs_num+=content.count(seg)
    
    #每段平均文字数
    mid_word_num=wordLen/paraNum
    
    return content.strip(),paraNum,wordLen,cn_segs_num,segs_num,mid_word_num