#-*- coding:utf-8-*-
#author:zhang_cs
#date:207-07-29 13:58:06 
import sys

def get_exce_info(exc_info):
    """
        输入为异常信息对象，输出为发生异常的文件名、行号
    """
    #exc_info:异常类型，异常，traceback对象
    traceObj = exc_info[2]          #traceback对象
    frameObj = traceObj.tb_frame    #获取frame对象，即本函数的frame信息
    f_code = frameObj.f_code       #获取该代码段的frame信息，即调用该函数的函数frame
    exce_filename=f_code.co_filename;
    exce_linename=frameObj.f_lineno
    return exce_filename,exce_linename
    
if __name__=="__main__":
    import emp
    try:  
        emp.test()  
    except:  
        exc_info = sys.exc_info()
        print get_exce_info(exc_info)