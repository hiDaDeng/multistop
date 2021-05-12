from multistop import Stopwords



#初始化，默认lang='chinese'
sw = Stopwords()

#查看支持的语言个数
print(len(sw.languages()))

#查看支持的语言
print(sw.languages())

#设置语言
sw.setlang(lang='chinese')

#查看当前语言的停用词表
print(sw.stopwords())

#停用词表中是否含有  【6啊】
print(sw.contains('6啊'))

#停用词表长度
print(sw.size())

#添加新停用词
sw.add('haohoaho')

#更新停用词表后的长度
print(sw.size())

