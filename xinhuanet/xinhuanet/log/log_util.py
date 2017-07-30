# -*- coding: utf-8 -*-
"""使用开源工具logbook实现日志记录、过期日志删除功能"""
import os
import sys
import inspect
from xinhuanet.utils.exce_info import exce_parse
from logbook import Logger,TimedRotatingFileHandler

this_file = inspect.getfile(inspect.currentframe())
path = os.path.abspath(os.path.dirname(this_file))
path+=os.sep+"logs"

#定义logbook日志记录句柄
logger=Logger("中搜Demo--xinhuanet")

def register_handlers():
    try:
        sys_handler = TimedRotatingFileHandler(path+os.sep+'sys_logs.txt',\
                        level="DEBUG",date_format='%Y-%m-%d',backup_count=30)
        sys_handler.push_application()
        
        info_handler = TimedRotatingFileHandler(path+os.sep+'info_logs.txt',\
                        level="INFO",date_format='%Y-%m-%d',backup_count=30)
        info_handler.push_application()

        error_handler = TimedRotatingFileHandler(path+os.sep+'error_logs.txt',\
                        level="ERROR",date_format='%Y-%m-%d',backup_count=30)
        error_handler.push_application()
    except :
        write_err("handers注册失败，请检查！:"+exce_parse.get_exce_info(sys.exc_info()))
        print "handers注册失败，请检查！:"+exce_parse.get_exce_info(sys.exc_info())
        exit(0)

def write_info(text):
    if text:
        logger.info(text)
        
def write_sys(text):
    if text:
        logger.debug(text)
        
def write_err(text):
    if text:
        logger.error(text)


if __name__=="__main__":
    write_info("hello_info")
    write_sys("hello_sys")
    write_err("hello_error")