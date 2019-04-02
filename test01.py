#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Theodore Sun
# datetime:2018/12/12 15:53
# software: PyCharm

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 生产-1到1之间的100个数作为x
train_X = np.linspace(-1, 1, 100)
# y = 2x,并且加入噪声处理
train_Y = 2 * train_X + np.random.randn(*train_X.shape) * 0.3

plt.plot(train_X, train_Y, 'ro', label='Original data')
plt.legend()
plt.show()

import re
validate_key = re.compile(r"^[\w\.\-\:\_]+$", re.UNICODE)
print(not validate_key.match("123"))
print(not validate_key.match("?"))
print(not validate_key.match(u"三"))
