#-*- coding:utf-8-*-

import urlparse


def filter_invalid_urls(urls,resurl):
    """
        需要进行URL转换和规范化格式，尚未完成
        去除无效的url

        常见的不规范的url为
            锚：#tag
            js:javascript:void(0)
            其他的暂时没有碰到，碰到会另外加入

    :param urls:从某页面抽取出的链接
    :param resurl:该页面链接
    :return:该页面中抽取出的非重复有效链接
    """

    #init
    valid_urls=[]

    # 保存链接信息
    for url in urls:
        url=url.encode("gb18030")
        if len(str(url).strip()) < 10:  # 长度太短的，过滤掉
            # print 'filter:%s len is short'%(url)
            continue
        if str(url).lstrip()[0] == '#':  # 过滤锚
            # print 'filter:%s startswith #'%(url)
            continue
        if str(url).lstrip()[:4] == "java":  # 过滤js调用
            # print 'filter:%s javascript'%(url)
            continue
        '''
        所有的去重操作都交给调度器来做，其他地方不做去重处理
        if ismember(get_md5(url.encode('UTF-8')),dupname,redisClient):#去重处理
        # print "dup",url
        # print 'filter:%s has crawled'%(url)
        continue  # 刚刚爬取过的目录页
        '''
        if not url.startswith("http://"):
            url = urlparse.urljoin(resurl, url)
        # print 'crawl %s'%(url)
        valid_urls.append(url)

    return valid_urls