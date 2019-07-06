#!/usr/bin/python
#coding=utf-8

#环境配置
#http://deron.meranda.us/python/demjson/
#在使用 Python 编码或解码 JSON 数据前，我们需要先安装 JSON 模块。本教程我们会下载 Demjson 并安装：
#$tar xvfz demjson-1.6.tar.gz
#$cd demjson-1.6
#$python setup.py install

#import demjson

#JSON函数
#函数      描述
#encode   将 Python 对象编码成 JSON 字符串
#decode   将已编码的 JSON 字符串解码为 Python 对象

#encode
#Python encode() 函数用于将 Python 对象编码成 JSON 字符串。
#语法
#demjson.encode(self, obj, nest_level=0)

#data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
#json = demjson.encode(data)
#print json

#decode
#Python 可以使用 demjson.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型。
#语法
#demjson.decode(self, txt)

#实例
#以下实例展示了Python 如何解码 JSON 对象：
#json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
#text = demjson.decode(json)
#print text
