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
    tr4w.analyze(text=text, lower=True, window=2)  # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
    
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
        res+=item.sentence  # index是语句在文本中位置，weight是权重
    return res

if __name__=="__main__":
    text="""新华社北京7月21日电（顾江冰、魏梦佳）21日，来自北京、香港、澳门三地300多名青年学生相聚北京语言大学，共同参加第22届“我的祖国—京港澳学生交流营”开营式。未来一周，青年学生们将在北京参加多项活动，增进交流互动，共同了解祖国的历史和发展。 据悉，此届交流营共设10个团队，营员们将在活动期间参观中国人民抗日战争纪念馆、国家博物馆、北京排水科普馆、圆明园等，聆听“一国两制”和外交事务专题讲座并参加小组主题调研等活动。这些活动在帮助学生增长知识的同时，也为他们提供展示能力素质和增进友谊的机会。 开营仪式上，教育部港澳台事务办公室常务副主任赵灵山在致辞中表示，京港澳学生交流营是内地、港澳青年交流和沟通的品牌活动，将青年学生的个人生涯规划和国家命运、香港和澳门的未来发展连接起来。大批青年学子通过这项活动亲身感受到中华民族悠久灿烂的历史文化，增强了民族自信心和自豪感，也认识到自己的责任。 北京语言大学校长刘利表示，今年是此项活动举办的第22年，恰逢香港回归祖国20周年，“希望三地青年学子能充分利用京港澳交流营这个难得的平台增进沟通、增进交流，共同探讨祖国未来发展命题，共同担当时代赋予的责任和使命，为实现中华民族伟大复兴不断奋斗。” “我将来很想到内地上大学。”澳门营员代表林依蓝说，“内地与港澳学习方式不同，我想通过这个平台和内地的优秀学生多交流，学习他们的经验，将来实现更好的发展。” 该交流营创办于1994年。20多年来，这项活动影响广泛，已成为京港澳学生增进了解交流的品牌项目。截至目前，已有5000多名三地青年参加了交流营活动，其中港澳学生达3000多名。（完）""".decode("gb18030")
    print '123'
    print parse_keywords_textrank(text)
    print parse_abstract_textrank(text)