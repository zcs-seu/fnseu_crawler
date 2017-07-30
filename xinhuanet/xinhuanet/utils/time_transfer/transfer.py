#-*- coding:utf-8-*-
import time
def transfer_time(datestring,dateformat,destdateformat):
    """
    判断url中的时间格式是否符合预期，若符合预期则转换为目标时间格式，否则返回None
    :param datestring:
    :return:
    """
    try:
        timeArray = time.strptime(datestring, dateformat)
        date = time.strftime(destdateformat, timeArray)
    except Exception,e:
        date = None
    return date