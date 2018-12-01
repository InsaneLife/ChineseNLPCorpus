# 中文文本分类数据集

数据来源：

今日头条客户端



数据格式：

```
6552431613437805063_!_102_!_news_entertainment_!_谢娜为李浩菲澄清网络谣言，之后她的两个行为给自己加分_!_佟丽娅,网络谣言,快乐大本营,李浩菲,谢娜,观众们
```

每行为一条数据，以`_!_`分割的个字段，从前往后分别是 新闻ID，分类code（见下文），分类名称（见下文），新闻字符串（仅含标题），新闻关键词



分类code与名称：

```
100 民生 故事 news_story
101 文化 文化 news_culture
102 娱乐 娱乐 news_entertainment
103 体育 体育 news_sports
104 财经 财经 news_finance
106 房产 房产 news_house
107 汽车 汽车 news_car
108 教育 教育 news_edu 
109 科技 科技 news_tech
110 军事 军事 news_military
112 旅游 旅游 news_travel
113 国际 国际 news_world
114 证券 股票 stock
115 农业 三农 news_agriculture
116 电竞 游戏 news_game
```



数据规模：

共382688条，分布于15个分类中。



采集时间：

2018年05月



实验结果：

以0.7 0.15 0.15做分割。欢迎提交你使用本数据集的实验结果~

```
Test Loss:   0.57, Test Acc:  83.81%

                    precision    recall  f1-score   support

        news_story       0.66      0.75      0.70       848

      news_culture       0.57      0.83      0.68      1531

news_entertainment       0.86      0.86      0.86      8078

       news_sports       0.94      0.91      0.92      7338

      news_finance       0.59      0.67      0.63      1594

        news_house       0.84      0.89      0.87      1478

          news_car       0.92      0.90      0.91      6481

          news_edu       0.71      0.86      0.77      1425

         news_tech       0.85      0.84      0.85      6944

     news_military       0.90      0.78      0.84      6174

       news_travel       0.58      0.76      0.66      1287

        news_world       0.72      0.69      0.70      3823

             stock       0.00      0.00      0.00        53

  news_agriculture       0.80      0.88      0.84      1701

         news_game       0.92      0.87      0.89      6244

       avg / total       0.85      0.84      0.84     54999



以上Acc较低的原因：

1，数据不均衡，部分类目数据太少

2，部分分类之间本身模棱两可，例如故事、文化、旅行

详见text-class xxxx内代码

后续可以优化的地方：

1，更多的数据

2，更全的分类

因为分类不全，例如缺少美食等，导致实际使用时，分哪里都不对的情况出现。

3，更均衡的分类数据

4，引入正文

```


### NLP chat group

Welcome

![](http://fate2.oss-cn-shanghai.aliyuncs.com/meta/qq-qun-nlp.jpeg)