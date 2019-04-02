#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Theodore Sun
# datetime:2018/12/19 15:41
# software: PyCharm

import collections
dic = collections.OrderedDict()
dic['a'] = 'a'
dic['b'] = 'b'

print(dict(wrapper=dict(a='a', b='b')))
print(dict(wrapper={'a': 'a', 'b': 'b'}))
print(dic)
print(type(dic))
print(dict(a='a', b='b'))

a1 = int(40)
b1 = int(10)

print(int(a1 / b1))
print(int(a1 % b1))

print(int((a1 + b1 - 1) / b1))


