# **ChineseNlpCorpus**

中文自然语言处理数据集，平时做做实验的材料。欢迎补充提交合并。

# 1. 文本分类

## 新闻分类

- 今日头条中文新闻（短文本）分类数据集 ：https://github.com/fateleak/toutiao-text-classfication-dataset
  - 数据规模：共382688条，分布于15个分类中。
  - 采集时间：2018年05月。
  - 以0.7 0.15 0.15做分割 。
- 清华新闻分类语料：http://thuctc.thunlp.org/#%E8%8E%B7%E5%8F%96%E9%93%BE%E6%8E%A5
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



# 2. 实体识别：

- ## 微博实体识别.

  - https://github.com/hltcoe/golden-horse

- ## boson数据。

  - 包含6种实体类型。
  - https://github.com/InsaneLife/ChineseNLPCorpus/tree/master/NER/MSRA/boson

- ## 1998年人民日报数据集。

  - 人名、地名、组织名三种实体类型 
  - https://github.com/InsaneLife/ChineseNLPCorpus/tree/master/NER/[renMinRiBao](https://github.com/InsaneLife/ChineseNLPCorpus/tree/master/NER/renMinRiBao) 

- ## MSRA微软亚洲研究院数据集。

  - 5 万多条中文命名实体识别标注数据（包括地点、机构、人物） 
  - https://github.com/InsaneLife/ChineseNLPCorpus/tree/master/NER/MSRA

# 3. 搜索匹配

## OPPO手机搜索排序

OPPO手机搜索排序query-title语义匹配数据集。

下载链接：https://pan.baidu.com/s/1Obm8oRVZEIh76-cpPc0qZw



## 网页搜索结果评价(SogouE)

- 用户查询及相关URL列表 

- https://www.sogou.com/labs/resource/e.php

# 4. 推荐系统

| 数据集      | 数据概览                                                     | 下载地址                                                     |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ez_douban   | 5 万多部电影（3 万多有电影名称，2 万多没有电影名称），2.8 万 用户，280 万条评分数据 | [点击查看](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/ez_douban/intro.ipynb) |
| dmsc_v2     | 28 部电影，超 70 万 用户，超 200 万条 评分/评论 数据         | [点击查看](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/dmsc_v2/intro.ipynb) |
| yf_dianping | 24 万家餐馆，54 万用户，440 万条评论/评分数据                | [点击查看](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/yf_dianping/intro.ipynb) |
| yf_amazon   | 52 万件商品，1100 多个类目，142 万用户，720 万条评论/评分数据 | [点击查看](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/yf_amazon/intro.ipynb) |

# 5. 百科数据 

## 维基百科

维基百科会定时将语料库打包发布：

- [数据处理博客](https://blog.csdn.net/wangyangzhizhou/article/details/78348949)
- https://dumps.wikimedia.org/zhwiki/

## 百度百科

只能自己爬，爬取得链接：`https://pan.baidu.com/share/init?surl=i3wvfil`提取码 neqs 。 



# 6. 预训练：（词向量or模型）

## BERT

1. 开源代码：https://github.com/google-research/bert
2. 模型下载：[**BERT-Base, Chinese**](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip): Chinese Simplified and Traditional, 12-layer, 768-hidden, 12-heads, 110M parameters



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