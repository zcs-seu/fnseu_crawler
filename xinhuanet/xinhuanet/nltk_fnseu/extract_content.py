#-*- coding:utf-8-*-
import sys
from xinhuanet.nltk_fnseu.content_tools import content_goose, content_boilerpipe, content_readability, judge_type
from xinhuanet.nltk_fnseu.content_tools.bs_proc import get_bs_by_html
from xinhuanet.nltk_fnseu.content_tools.content_tools import content_format
from xinhuanet.nltk_fnseu.content_tools.html_proc import removeTags
from xinhuanet.nltk_fnseu.content_tools.judge_type import predict_type
from xinhuanet.log import log_util
from xinhuanet.utils.exce_info import exce_parse

def parse_content(html,hxs,url_ctype):
    """
        新闻、政府网站类网页正文抽取的对外接口函数
        三种抽取正文方式（goose/boilerpipe/readability）底层实现的集成调用接口
        :param sourceHtml:待抽取网页源码
        :returns:str— —网页中的正文信息，若未找到则返回""
    """
    try:
        bs =get_bs_by_html(html)
        sourceHtml=str(bs)


        #抽取正文
        try:
            # goose抽取正文
            content = content_goose.get_content_by_html(sourceHtml);
            g_content, g_paraNum, g_wordLen, g_cn_segs_num, g_segs_num, g_mid_word_num = \
                content_format(content.strip())
        except:
            g_content, g_paraNum, g_wordLen, g_cn_segs_num, g_segs_num, g_mid_word_num = \
                "", 0, 0, 0, 0, 0;

        # boilerpipe抽取正文
        content = content_boilerpipe.get_content_by_html(sourceHtml);
        b_content, b_paraNum, b_wordLen, b_cn_segs_num, b_segs_num, b_mid_word_num = \
            content_format(content.strip())

        # 生成网页特征向量
        x = [
            g_paraNum, g_wordLen, g_cn_segs_num, g_segs_num, g_mid_word_num,
            b_paraNum, b_wordLen, b_cn_segs_num, b_segs_num, b_mid_word_num,
            b_paraNum, b_wordLen, b_cn_segs_num, b_segs_num, b_mid_word_num
        ]
        content = get_result_content(x, g_content, b_content, b_content);
    except:
        log_util.write_err("正文解析失败:"+exce_parse.get_exce_info(sys.exc_info()))

    if not content:
        return None;
    return content;

def get_result_content(x,g_content,b_content,r_content):
    """
        判断最终应该使用哪一种抽取方式
        :param x:待判断网页的特征向量
        :param g_content:goose抽取出正文文
        :param b_content:boilerpipe抽取出正文
        :param r_content:boilerpipe抽取出正文
        :returns:str— —最后选择的网页正文（未规范化）
    """
    type=0
    try:
        type=predict_type(x);
    except Exception,e:
        print e
    content=""
    if type==0:content=g_content;
    if type==1:content=g_content;
    if type==2:content=b_content;
    if type==3:content=r_content;
    if len(content.encode("utf8"))<200:
        return ""
    if content:
        return content
    else:
        return ""

if __name__=="__main__":
    import urllib2
    html=urllib2.urlopen("http://news.xinhuanet.com/world/2017-07/01/c_1121247366.htm").read()
    print parse_content(html.decode("utf8"),None,None)