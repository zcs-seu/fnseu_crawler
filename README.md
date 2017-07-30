# 项目简介
1. 项目应用范围
```
（1）实现对新华网的定制化分布式采集、解析；
（2）实现基于redis实现的BloomFilter的URL去重，支持多Spider共用或者单独使用BloomFilter选择；
（3）实现基于logbook的日志系统的日志记录统一管理、过期日志（30）删除功能；
（4）实现配置统一管理功能，简单几步即可实现对当前新华网采集模块的拓展；
（5）实现标题、正文、时间、作者、编辑、来源、一级类别、二级类别、关键词、摘要等信息的自动解析；
    ...
```

2. 免责声明
```
    本采集模块主要使用jieba、goose、boilerpipe、textrankZH、scikit-learn等开源框架以及
mongodbDB、redis等开源工具实现。
    本模块开源的目的主要是供从事或将从事信息采集工作的学生、新手学习之用，不得用于谋取
不正当经济利益，特此声明。
```

3. 依赖说明
```
    本项目使用Python语言，基于Scrapy-Redis框架实现，开发环境为Ubuntu、Python 2.7，
主要依赖的工具包有：
    （1）redis
    （2）pymongo
    （3）chardet
    （4）time
    （5）urlparse
    （6）Scrapy-Redis
    （7）goose
    （8）boilerpipe
```

4. 使用说明
```
（1）用于单击新华网采集
    i.   git clone https://github.com/zcs-seu/fnseu_crawler.git ；
    ii.  安装依赖；
    iii. cd xinhuanet；
    iv.  python run.py；
（2）用于分布式新华网采集
    i.   各机器分别执行：git clone https://github.com/zcs-seu/fnseu_crawler.git；
    ii.  各机器分别执行：安装依赖；
    iii. 修改configure.xml中的crawler_id，各机器之间不能重复；
    iv.  各机器分别执行：cd xinhuanet；
    v.   各机器分别执行：python run.py；
（3）扩展至其他网站采集（假设已经克隆并解决依赖，此处仅给出扩展方法）：
    i.   修改configure.xml中的crawler_id、crawler_name等与爬虫命名相关的配置信息；
    ii.  修改configure.xml中dbs中数据库相关配置信息；
    iii. 修改configure.xml中start_urls、allowed_domains等与爬取网站相关的配置信息；
    iv.  修改configure.xml中keywords_rules、title_rules等与语义解析相关的xpath配置信息；
    v.   修改configure.xml中allowed_channels等频道配置信息及频道特有语义解析规则配置信息；
（4）扩展其他语义解析（假设已经克隆并解决依赖，此处仅给出扩展方法）：
    i.   在configure.xml中的public_rules中添加扩展的语义解析规则；
    ii.  在configure.xml中的allowed_channels中添加频道特有的语义解析规则；
    iii. 启动爬虫
```