#-*- coding:utf-8-*-
#author:zhang_cs
#date:207-07-29 13:58:06 
import sys

def get_exce_info(exc_info):
    """
        ����Ϊ�쳣��Ϣ�������Ϊ�����쳣���ļ������к�
    """
    #exc_info:�쳣���ͣ��쳣��traceback����
    traceObj = exc_info[2]          #traceback����
    frameObj = traceObj.tb_frame    #��ȡframe���󣬼���������frame��Ϣ
    f_code = frameObj.f_code       #��ȡ�ô���ε�frame��Ϣ�������øú����ĺ���frame
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