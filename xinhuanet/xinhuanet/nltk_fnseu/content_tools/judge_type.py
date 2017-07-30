#!usr/local/bin/python
#-*-coding:utf-8-*-
"""

    利用朴素贝叶斯确定选择goose、boilerpipe、readability正文抽取算法的正文抽取结果中的一种。
    目前使用的特征：
        （1）goose段落数
        （2）goose文字数
        （3）goose标点数
        （4）goose中文标点数
        （5）goose每段平均段落数
        （1）boilerpipe段落数
        （2）boilerpipe文字数
        （3）boilerpipe标点数
        （4）boilerpipe中文标点数
        （5）boilerpipe每段平均段落数
        （1）readability段落数
        （2）readability文字数
        （3）readability标点数
        （4）readability中文标点数
        （5）readability每段平均段落数
"""
import os
import sys
import inspect
from sklearn.externals import joblib
from xinhuanet.log import log_util
from xinhuanet.utils.exce_info import exce_parse
this_file = inspect.getfile(inspect.currentframe())
path = os.path.abspath(os.path.dirname(this_file))

def predict_type(x):
    """
        利用朴素贝叶斯模型用于选择goose、boilerpipe、readability以及自主开发的
        基于行块密度的正文抽取算法的正文抽取结果中的一种。
        :returns:int— — 0表示选择自主实现的基于行块密度的抽取结果
                        1表示选择goose抽取结果
                        2表示选择boilerpipe抽取结果
                        3表示选择readability抽取结果
    """
    try:
        model = joblib.load(path+os.sep+"models/nb/nb.pkl")
        predicted = model.predict(x)
        return predicted[0]
    except:
        log_util.write_err("训练好的朴素贝叶斯分类器模型没有找到，请查看位置是否正确:"\
        +exce_parse.get_exce_info(sys.exc_info()))
        exit(0)
