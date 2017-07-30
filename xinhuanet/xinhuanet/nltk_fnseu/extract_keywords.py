#-*- coding:utf-8-*-
import jieba
import jieba.analyse
from xinhuanet.config.config import DetailRule


def parse_keywords(html,hxs,url_ctype):
    keywords_rules = DetailRule.allowed_channels[url_ctype]["keywords_rules"]
    for rule_id in keywords_rules:
        xpath = keywords_rules[rule_id]["xpath"]
        keywords_sep = keywords_rules[rule_id]["sep"]
        try:
            keywords_str = hxs.select(xpath).extract()[0].strip()
            if keywords_str:
                return keywords_str.split(keywords_sep)
        except Exception, e:
            continue;
    
    return []

def parse_keywords_textrank(text):
    res=jieba.analyse.extract_tags(text, topK=5, withWeight=False, allowPOS=())
    if res:     
        return res
    
    import sys
    try:
        reload(sys)
        sys.setdefaultencoding('utf-8')
    except:
        pass
    
    from textrank4zh import TextRank4Keyword, TextRank4Sentence

    res=[]
    tr4w = TextRank4Keyword()
    tr4w.analyze(text=text, lower=True, window=2)  # py2��text������utf8�����str����unicode����py3�б�����utf8�����bytes����str����
    
    for item in tr4w.get_keywords(20, word_min_len=1):
        res.append(item.word)
    if len(res)>5:
        res=res[0:5]
    return res

def parse_abstract_textrank(text):
    import sys
    try:
        reload(sys)
        sys.setdefaultencoding('utf-8')
    except:
        pass
    
    from textrank4zh import TextRank4Keyword, TextRank4Sentence

    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source = 'all_filters')

    res=""
    for item in tr4s.get_key_sentences(num=3):
        res+=item.sentence  # index��������ı���λ�ã�weight��Ȩ��
    return res

if __name__=="__main__":
    text="""�»��籱��7��21�յ磨�˽�����κ�μѣ�21�գ����Ա�������ۡ���������300��������ѧ����۱������Դ�ѧ����ͬ�μӵ�22�조�ҵ���������۰�ѧ������Ӫ����Ӫʽ��δ��һ�ܣ�����ѧ���ǽ��ڱ����μӶ���������������������ͬ�˽��������ʷ�ͷ�չ�� ��Ϥ���˽콻��Ӫ����10���Ŷӣ�ӪԱ�ǽ��ڻ�ڼ�ι��й�������ս������ݡ����Ҳ���ݡ�������ˮ���չݡ�Բ��԰�ȣ�������һ�����ơ����⽻����ר�⽲�����μ�С��������еȻ����Щ��ڰ���ѧ������֪ʶ��ͬʱ��ҲΪ�����ṩչʾ�������ʺ���������Ļ��ᡣ ��Ӫ��ʽ�ϣ��������۰�̨����칫�ҳ�����������ɽ���´��б�ʾ�����۰�ѧ������Ӫ���ڵء��۰����꽻���͹�ͨ��Ʒ�ƻ��������ѧ���ĸ������Ĺ滮�͹������ˡ���ۺͰ��ŵ�δ����չ������������������ѧ��ͨ������������ܵ��л������ƾò��õ���ʷ�Ļ�����ǿ�����������ĺ��Ժ��У�Ҳ��ʶ���Լ������Ρ� �������Դ�ѧУ��������ʾ�������Ǵ����ٰ�ĵ�22�꣬ǡ����ۻع����20���꣬��ϣ����������ѧ���ܳ�����þ��۰Ľ���Ӫ����ѵõ�ƽ̨������ͨ��������������ͬ̽�����δ����չ���⣬��ͬ����ʱ����������κ�ʹ����Ϊʵ���л�����ΰ���˲��Ϸܶ����� ���ҽ������뵽�ڵ��ϴ�ѧ��������ӪԱ����������˵�����ڵ���۰�ѧϰ��ʽ��ͬ������ͨ�����ƽ̨���ڵص�����ѧ���ཻ����ѧϰ���ǵľ��飬����ʵ�ָ��õķ�չ���� �ý���Ӫ������1994�ꡣ20������������Ӱ��㷺���ѳ�Ϊ���۰�ѧ�������˽⽻����Ʒ����Ŀ������Ŀǰ������5000������������μ��˽���Ӫ������и۰�ѧ����3000���������꣩""".decode("gb18030")
    print '123'
    print parse_keywords_textrank(text)
    print parse_abstract_textrank(text)