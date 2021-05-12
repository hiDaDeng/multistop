from setuptools import setup
import setuptools

setup(
    name='multistop',     # 包名字
    version='1.0',   # 包版本
    description='文本分析停用词表，支持中英德法等15种语言。',   # 简单描述
    author='大邓',  # 作者
    author_email='thunderhit@qq.com',  # 邮箱
    url='https://github.com/thunderhit/cnstopwords',      # 包的主页
    packages=setuptools.find_packages(),
    package_data = {'':['dict.json']},  #所有目录下的json词典文件
    install_requires=['jieba', 'numpy'],
    python_requires='>=3.5',
    license="MIT",
    keywords=['chinese text analysis', 'text analysis', 'text mining', 'stopwords',  'natural language processing'],
    long_description=open('README.md').read(), # 读取的Readme文档内容
    long_description_content_type="text/markdown")  # 指定包文档格式为markdown
    #py_modules = ['eventextraction.py']
