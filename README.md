

# 一、multistop

停用词表, 同时支持中英德等15种语言。

<br>

<br>



# 二、安装

```
pip3 install multistop
```



# 三、使用

初始化停用词类

```
from multistop import Stopwords
#默认选取的中文lang='chinese'
sw = Stopwords()
```



<br>

查看支持的语言

```
sw.languages()
```

Run

```
dict_keys(['dutch', 'german', 'hungarian', 'turkish', 'russian', 'italian', 'english', 'norwegian', 'portuguese', 'finnish', 'danish', 'french', 'swedish', 'spanish', 'chinese'])

```



<br>

选择某种语言的停用词表

```
sw.setlang(lang='chinese')
```

Run

```
set language to chinese
```



<br>



词表长度

```
sw.size()
```



Run

```
778
```



<br>

查看停用词表是否含有某词

```
sw.contains('的')
```

Run

```
True
```



<br>



添加新停用词

```
sw.add('6啊')
sw.size()
```

Run

```
779
```



<br>



将停用词表下载下来

```
sw.download('chinese.txt')
```



<br>

<br>

# 如果

如果您是经管人文社科专业背景，编程小白，面临海量文本数据采集和处理分析艰巨任务，可以参看[《python网络爬虫与文本数据分析》](https://ke.qq.com/course/482241?tuin=163164df)视频课。作为文科生，一样也是从两眼一抹黑开始，这门课程是用五年时间凝缩出来的。自认为讲的很通俗易懂o(*￣︶￣*)o，

- python入门
- 网络爬虫
- 数据读取
- 文本分析入门
- 机器学习与文本分析
- 文本分析在经管研究中的应用

感兴趣的童鞋不妨 戳一下[《python网络爬虫与文本数据分析》](https://ke.qq.com/course/482241?tuin=163164df)进来看看~

[![](img/课程.png)](https://ke.qq.com/course/482241?tuin=163164df)



# 更多

- [B站:大邓和他的python](https://space.bilibili.com/122592901/channel/detail?cid=66008)

- 公众号：大邓和他的python

- [知乎专栏：数据科学家](https://zhuanlan.zhihu.com/dadeng)

<br>

![](img/大邓和他的Python.png)