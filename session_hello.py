#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Theodore Sun
# datetime:2018/12/31 14:55
# software: PyCharm

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 定义常量
hello = tf.constant("Hello, TensorFlow!")
# 建立一个session
session = tf.Session()
# 通过session里面的run函数来运行结果
print(session.run(hello))
# 关闭session
session.close()

a = tf.constant(3)
b = tf.constant(4)
with tf.Session() as sess:
    print("相加：%i" % sess.run(a + b))
    print("相乘：%i" % sess.run(a * b))

a1 = tf.placeholder(tf.int16)
b1 = tf.placeholder(tf.int16)
add = tf.add(a1, b1)
mul = tf.multiply(a1, b1)
with tf.Session() as sess:
    print("相加：%i" % sess.run(add, feed_dict={a1: 3, b1: 4}))
    print("相乘：%i" % sess.run(mul, feed_dict={a1: 3, b1: 4}))
    print(sess.run([add, mul], feed_dict={a1: 3, b1: 4}))
