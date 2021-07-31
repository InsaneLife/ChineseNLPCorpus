[TOC]


# ChineseNlpCorpus

中文自然语言处理数据集，平时做做实验的材料。欢迎补充提交合并。

# 阅读理解

## 百度千言

百度的千言数据集，可以用来做中文阅读理解实验，主要包含：

- $DuReader_{robust}$:单篇章、抽取式阅读理解数据集，数据集详细参考[论文](https://arxiv.org/abs/2004.11142)
- $DuReader_{yesno}$:观点型阅读理解数据集，主要是极性，肯定、否定和无法确定/分情况
- $DuReader_{checklist}$: 抽取式数据集，[详细](https://github.com/PaddlePaddle/Research/tree/master/NLP/DuReader-Checklist-BASELINE)

[数据集下载](https://aistudio.baidu.com/aistudio/competition/detail/49/?isFromLUGE=TRUE)

# 任务型对话数据

## Medical DS

复旦大学发布的基于百度拇指医生上真实对话数据的，面向任务型对话的中文医疗诊断数据集。

| 名称       | 规模                       | 创建日期 | 作者       | 单位     | 论文                                                         | 下载                                                         |
| ---------- | -------------------------- | -------- | ---------- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Medical DS | 710个对话 67种症状 4种疾病 | 2018年   | Liu et al. | 复旦大学 | [链接](http://www.sdspeople.fudan.edu.cn/zywei/paper/liu-acl2018.pdf) | [链接](http://www.sdspeople.fudan.edu.cn/zywei/data/acl2018-mds.zip) |

## 千言数据集

包含知识对话、推荐对话、画像对话。详细见[官网](https://aistudio.baidu.com/aistudio/competition/detail/48/?isFromLUGE=TRUE)

## [CATSLU](https://dl.acm.org/doi/10.1145/3340555.3356098)

之前的一些对话数据集集中于语义理解，而工业界真实情况ASR也会有错误，往往被忽略。[CATSLU](https://dl.acm.org/doi/10.1145/3340555.3356098)而是一个中文语音+NLU文本理解的对话数据集，可以从语音信号到理解端到端进行实验，例如直接从音素建模语言理解（而非word or token）。

数据统计：

![image-20200910233858454](https://raw.githubusercontent.com/InsaneLife/ChineseNLPCorpus/master/pic/image-20200910233858454.png)

官方说明手册：[CATSLU](https://sites.google.com/view/catslu/handbook)
数据下载：[https://sites.google.com/view/CATSLU/home](https://sites.google.com/view/CATSLU/home)

## NLPCC2018 Shared Task 4

中文呢真实商用车载语音任务型对话系统的对话日志

## SMP

这是一系类数据集，每年都会有新的数据集放出。
### SMP-2020-ECDT小样本对话语言理解数据集
> 论文中叫FewJoint 基准数据集，来自于讯飞AIUI开放平台上真实用户语料和专家构造的语料(比例大概为3：7)，包含59个真实domain，目前domain最多的对话数据集之一，可以避免构造模拟domain，非常适合小样本和元学习方法评测。其中45个训练domain，5个开发domain，9个测试domain。

数据集介绍：[新闻链接](https://mp.weixin.qq.com/s?__biz=MzIxMjAzNDY5Mg==&mid=2650799572&idx=1&sn=509e256c62d80e2866f38e9d026d4af3&chksm=8f47683fb830e129f0ac7d2ff294ad1bd2cad5dc2050ae1ab81a7b108b79a6edcdba3d8030f9&mpshare=1&scene=1&srcid=1007YJCULNtwsRCUx7b35S0m&sharer_sharetime=1602603945222&sharer_shareid=904fa30621d7b898b031f4fdb5da41fc&key=9ae93b5dab71cae000c0dd901c537565d9fac572f40bafa92d79cee849b96fddbdece4d7151bec0f9a1c330dc3a9ddfe5ff4d742eef3165a71be493cd344e6ebc0a34dd5ebc61cb3c519f3a1d765f480cd5fd85d6b45655cc09b9816726ff06c2480b5287346c11ef1a18c0195b51259bd768110b49eb4b7583b40580369bcd2&ascene=1&uin=MTAxMzA5NjY2NQ%3D%3D&devicetype=Windows+10+x64&version=6300002f&lang=zh_CN&exportkey=ATbSQY9SBUjBETt7KZpV%2BIk%3D&pass_ticket=gGOfSeYJMhUPfn3Fbu8lBtWlGjw%2BANSIQ4rgajKq6vxzOW%2Fm%2Bwcw3YkXM0bkiM%2Bz&wx_header=0)

数据集论文：https://arxiv.org/abs/2009.08138
数据集下载地址：https://atmahou.github.io/attachments/FewJoint.zip
小样本工具平台主页地址：https://github.com/AtmaHou/MetaDialog

### SMP-2019-NLU
包含领域分类、意图识别和语义槽填充三项子任务的数据集。训练数据集下载：[trian.json](./dialogue/SMP-2019-NLU/train.json)，目前只获取到训练集，如果有同学有测试集，欢迎提供。

|        | Train |
| ------ | ----- |
| Domain | 24    |
| Intent | 29    |
| Slot   | 63    |
| Samples   | 2579  |



### SMP-2017
中文对话意图识别数据集，官方git和数据: [https://github.com/HITlilingzhi/SMP2017ECDT-DATA](https://github.com/HITlilingzhi/SMP2017ECDT-DATA)

数据集：

|               | Train |
| ------------- | ----- |
| Train samples | 2299  |
| Dev samples   | 770   |
| Test samples  | 666   |
| Domain        | 31    |

论文：[https://arxiv.org/abs/1709.10217  ](https://arxiv.org/abs/1709.10217)

# 文本分类

## 新闻分类

- 今日头条中文新闻（短文本）分类数据集 ：https://github.com/fateleak/toutiao-text-classfication-dataset
  - 数据规模：共**38万条**，分布于15个分类中。
  - 采集时间：2018年05月。
  - 以0.7 0.15 0.15做分割 。
- 清华新闻分类语料：
  - 根据新浪新闻RSS订阅频道2005~2011年间的历史数据筛选过滤生成。
  - 数据量：**74万篇新闻文档**（2.19 GB）
  - 小数据实验可以筛选类别：体育, 财经, 房产, 家居, 教育, 科技, 时尚, 时政, 游戏, 娱乐
  - http://thuctc.thunlp.org/#%E8%8E%B7%E5%8F%96%E9%93%BE%E6%8E%A5
  - rnn和cnn实验：https://github.com/gaussic/text-classification-cnn-rnn
- 中科大新闻分类语料库：http://www.nlpir.org/?action-viewnews-itemid-145



## 情感/观点/评论 倾向性分析

| 数据集                  | 数据概览                                                     | 下载                                                         |
| ----------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ChnSentiCorp_htl_all    | 7000 多条酒店评论数据，5000 多条正向评论，2000 多条负向评论  | [地址](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/ChnSentiCorp_htl_all/intro.ipynb) |
| waimai_10k              | 某外卖平台收集的用户评价，正向 4000 条，负向 约 8000 条      | [地址](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/waimai_10k/intro.ipynb) |
| online_shopping_10_cats | 10 个类别，共 6 万多条评论数据，正、负向评论各约 3 万条， 包括书籍、平板、手机、水果、洗发水、热水器、蒙牛、衣服、计算机、酒店 | [地址](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/online_shopping_10_cats/intro.ipynb) |
| weibo_senti_100k        | 10 万多条，带情感标注 新浪微博，正负向评论约各 5 万条        | [地址](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/weibo_senti_100k/intro.ipynb) |
| simplifyweibo_4_moods   | 36 万多条，带情感标注 新浪微博，包含 4 种情感， 其中喜悦约 20 万条，愤怒、厌恶、低落各约 5 万条 | [地址](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/simplifyweibo_4_moods/intro.ipynb) |
| dmsc_v2                 | 28 部电影，超 70 万 用户，超 200 万条 评分/评论 数据         | [地址](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/dmsc_v2/intro.ipynb) |
| yf_dianping             | 24 万家餐馆，54 万用户，440 万条评论/评分数据                | [地址](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/yf_dianping/intro.ipynb) |
| yf_amazon               | 52 万件商品，1100 多个类目，142 万用户，720 万条评论/评分数据 | [地址](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/yf_amazon/intro.ipynb) |
| 百度千言情感分析数据集  | 包括句子级情感分类（Sentence-level Sentiment Classification）、评价对象级情感分类（Aspect-level Sentiment Classification）、观点抽取（Opinion Target Extraction） | [地址](https://aistudio.baidu.com/aistudio/competition/detail/50/?isFromLUGE=TRUE) |





# 实体识别&词性标注&分词

- ## 微博实体识别.

  - https://github.com/hltcoe/golden-horse

- ## boson数据。

  - 包含6种实体类型。
  - https://github.com/InsaneLife/ChineseNLPCorpus/tree/master/NER/boson

- ## 人民日报数据集。

  - 人名、地名、组织名三种实体类型 
  - 1998：[https://github.com/InsaneLife/ChineseNLPCorpus/tree/master/NER/renMinRiBao](https://github.com/InsaneLife/ChineseNLPCorpus/tree/master/NER/renMinRiBao) 
  - 2004：https://pan.baidu.com/s/1LDwQjoj7qc-HT9qwhJ3rcA password: 1fa3
- ## MSRA微软亚洲研究院数据集。

  - 5 万多条中文命名实体识别标注数据（包括地点、机构、人物） 
  - https://github.com/InsaneLife/ChineseNLPCorpus/tree/master/NER/MSRA

- SIGHAN Bakeoff 2005：一共有四个数据集，包含繁体中文和简体中文，下面是简体中文分词数据。

  -  MSR: <http://sighan.cs.uchicago.edu/bakeoff2005/>
  -  PKU ：<http://sighan.cs.uchicago.edu/bakeoff2005/> 

另外这三个链接里面数据集也挺全的，链接：

- [分词](https://github.com/luge-ai/luge-ai/blob/master/lexical-analysis/word-segment.md)
- [词性标注](https://github.com/luge-ai/luge-ai/blob/master/lexical-analysis/part-of-speech-tagging.md)
- [命名实体](https://github.com/luge-ai/luge-ai/blob/master/lexical-analysis/name-entity-recognition.md)

# 句法&语义解析

- [依存句法](https://github.com/luge-ai/luge-ai/blob/master/dependency-parsing/dependency-parsing.md)

## 语义解析

- 看方法主要还是转化为分类和ner任务。下载地址：[https://aistudio.baidu.com/aistudio/competition/detail/47/?isFromLUGE=TRUE](https://aistudio.baidu.com/aistudio/competition/detail/47/?isFromLUGE=TRUE)

| 数据集  | 单/多表 | 语言 | 复杂度 | 数据库/表格 | 训练集 | 验证集 | 测试集 | 文档                                                         |
| :-----: | :-----: | :--: | :----: | :---------: | :----: | :----: | :----: | ------------------------------------------------------------ |
| NL2SQL  |   单    | 中文 |  简单  | 5,291/5,291 | 41,522 | 4,396  | 8,141  | [NL2SQL](https://arxiv.org/abs/2006.06434)                   |
| CSpider |   多    | 中英 |  复杂  |   166/876   | 6,831  |  954   | 1,906  | [CSpider](https://arxiv.org/abs/1909.13293)                  |
|  DuSQL  |   多    | 中文 |  复杂  |   200/813   | 22,521 | 2,482  | 3,759  | [DuSQL](https://www.aclweb.org/anthology/2020.emnlp-main.562.pdf) |



# 信息抽取

- [实体链指](https://github.com/luge-ai/luge-ai/blob/master/information-extraction/entity_linking.md)
- [关系抽取](https://github.com/luge-ai/luge-ai/blob/master/information-extraction/relation-extraction.md)
- [事件抽取](https://github.com/luge-ai/luge-ai/blob/master/information-extraction/event-extraction.md)

# 搜索匹配

## 千言文本相似度

百度千言文本相似度，主要包含LCQMC/BQ Corpus/PAWS-X，见[官网](https://aistudio.baidu.com/aistudio/competition/detail/45/?isFromLUGE=TRUE)，丰富文本匹配的数据，可以作为目标匹配数据集的源域数据，进行多任务学习/迁移学习。

## OPPO手机搜索排序

OPPO手机搜索排序query-title语义匹配数据集。

链接:https://pan.baidu.com/s/1Hg2Hubsn3GEuu4gubbHCzw 提取码:7p3n


## 网页搜索结果评价(SogouE)

- 用户查询及相关URL列表 

- https://www.sogou.com/labs/resource/e.php

# 推荐系统

| 数据集      | 数据概览                                                     | 下载地址                                                     |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ez_douban   | 5 万多部电影（3 万多有电影名称，2 万多没有电影名称），2.8 万 用户，280 万条评分数据 | [点击查看](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/ez_douban/intro.ipynb) |
| dmsc_v2     | 28 部电影，超 70 万 用户，超 200 万条 评分/评论 数据         | [点击查看](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/dmsc_v2/intro.ipynb) |
| yf_dianping | 24 万家餐馆，54 万用户，440 万条评论/评分数据                | [点击查看](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/yf_dianping/intro.ipynb) |
| yf_amazon   | 52 万件商品，1100 多个类目，142 万用户，720 万条评论/评分数据 | [点击查看](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/yf_amazon/intro.ipynb) |

# 百科数据 

## 维基百科

维基百科会定时将语料库打包发布：

- [数据处理博客](https://blog.csdn.net/wangyangzhizhou/article/details/78348949)
- https://dumps.wikimedia.org/zhwiki/

## 百度百科

只能自己爬，爬取得链接：`https://pan.baidu.com/share/init?surl=i3wvfil`提取码 neqs 。 



# 指代消歧 

CoNLL 2012 ：<http://conll.cemantix.org/2012/data.html> 

# 预训练：（词向量or模型）

## BERT

1. 开源代码：https://github.com/google-research/bert
2. 模型下载：[**BERT-Base, Chinese**](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip): Chinese Simplified and Traditional, 12-layer, 768-hidden, 12-heads, 110M parameters

BERT变种模型：

| 模型                                                         | 参数 | git                                                          |
| ------------------------------------------------------------ | ---- | ------------------------------------------------------------ |
| [Chinese-BERT-base](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip) | 108M | [BERT](https://github.com/google-research/bert)              |
| [Chinese-BERT-wwm-ext](https://drive.google.com/open?id=1Jzn1hYwmv0kXkfTeIvNT61Rn1IbRc-o8) | 108M | [Chinese-BERT-wwm](https://github.com/ymcui/Chinese-BERT-wwm) |
| [RBT3](https://drive.google.com/open?id=1-rvV0nBDvRCASbRz8M9Decc3_8Aw-2yi) | 38M  | [Chinese-BERT-wwm](https://github.com/ymcui/Chinese-BERT-wwm) |
| [ERNIE 1.0 Base 中文](https://ernie-github.cdn.bcebos.com/model-ernie1.0.1.tar.gz) | 108M | [ERNIE](https://github.com/PaddlePaddle/ERNIE)、ernie模型转成tensorflow模型:[tensorflow_ernie](https://github.com/ArthurRizar/tensorflow_ernie) |
| [RoBERTa-large](https://drive.google.com/open?id=1W3WgPJWGVKlU9wpUYsdZuurAIFKvrl_Y) | 334M | [RoBERT](https://github.com/brightmart/roberta_zh)           |
| [XLNet-mid](https://drive.google.com/open?id=1342uBc7ZmQwV6Hm6eUIN_OnBSz1LcvfA) | 209M | [XLNet-mid](https://github.com/ymcui/Chinese-PreTrained-XLNet) |
| [ALBERT-large](https://storage.googleapis.com/albert_zh/albert_large_zh.zip) | 59M  | [Chinese-ALBERT](https://github.com/brightmart/albert_zh)    |
| [ALBERT-xlarge](https://storage.googleapis.com/albert_zh/albert_xlarge_zh_183k.zip) |      | [Chinese-ALBERT](https://github.com/brightmart/albert_zh)    |
| [ALBERT-tiny](https://storage.googleapis.com/albert_zh/albert_tiny_489k.zip) | 4M   | [Chinese-ALBERT](https://github.com/brightmart/albert_zh)    |
| [chinese-roberta-wwm-ext](https://www.paddlepaddle.org.cn/hubdetail?name=chinese-roberta-wwm-ext&en_category=SemanticModel) | 108M | [Chinese-BERT-wwm](https://github.com/ymcui/Chinese-BERT-wwm) |
| [chinese-roberta-wwm-ext-large](https://www.paddlepaddle.org.cn/hubdetail?name=chinese-roberta-wwm-ext-large&en_category=SemanticModel) | 330M | [Chinese-BERT-wwm](https://github.com/ymcui/Chinese-BERT-wwm) |

## ELMO

1. 开源代码：https://github.com/allenai/bilm-tf
2. 预训练的模型：https://allennlp.org/elmo

## 腾讯词向量

腾讯AI实验室公开的中文词向量数据集包含800多万中文词汇，其中每个词对应一个200维的向量。

- 下载地址：https://ai.tencent.com/ailab/nlp/embedding.html




## **上百种预训练中文词向量**

[https://github.com/Embedding/Chinese-Word-Vectors](https://link.zhihu.com/?target=https%3A//github.com/Embedding/Chinese-Word-Vectors)

# **中文完形填空数据集**

[https://github.com/ymcui/Chinese-RC-Dataset](https://link.zhihu.com/?target=https%3A//github.com/ymcui/Chinese-RC-Dataset)



# **中华古诗词数据库**

最全中华古诗词数据集，唐宋两朝近一万四千古诗人, 接近5.5万首唐诗加26万宋诗. 两宋时期1564位词人，21050首词。

[https://github.com/chinese-poetry/chinese-poetry](https://link.zhihu.com/?target=https%3A//github.com/chinese-poetry/chinese-poetry)



 

# **保险行业语料库**

[https://github.com/Samurais/insuranceqa-corpus-zh](https://link.zhihu.com/?target=https%3A//github.com/Samurais/insuranceqa-corpus-zh)

 

# **汉语拆字字典**

英文可以做char embedding，中文不妨可以试试拆字

[https://github.com/kfcd/chaizi](https://link.zhihu.com/?target=https%3A//github.com/kfcd/chaizi)

 



# 中文数据集平台

- ## **搜狗实验室**

  搜狗实验室提供了一些高质量的中文文本数据集，时间比较早，多为2012年以前的数据。

  [https://www.sogou.com/labs/resource/list_pingce.php](https://link.zhihu.com/?target=https%3A//www.sogou.com/labs/resource/list_pingce.php)

- ## **中科大自然语言处理与信息检索共享平台**

  [http://www.nlpir.org/?action-category-catid-28](https://link.zhihu.com/?target=http%3A//www.nlpir.org/%3Faction-category-catid-28)

- ## 中文语料小数据

  - 包含了中文命名实体识别、中文关系识别、中文阅读理解等一些小量数据。 
  - https://github.com/crownpku/Small-Chinese-Corpus

- ## 维基百科数据集

  - https://dumps.wikimedia.org/



# NLP工具

THULAC： [https://github.com/thunlp/THULAC](<https://github.com/thunlp/THULAC> ) ：包括中文分词、词性标注功能。

HanLP：<https://github.com/hankcs/HanLP> 

哈工大LTP <https://github.com/HIT-SCIR/ltp> 

NLPIR <https://github.com/NLPIR-team/NLPIR>

jieba <https://github.com/yanyiwu/cppjieba> 

百度千言数据集：[https://github.com/luge-ai/luge-ai](https://github.com/luge-ai/luge-ai)
