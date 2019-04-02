#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Theodore Sun
# datetime:2018/12/19 14:58
# software: PyCharm

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

plotdata = {"batchsize": [], "loss": []}


def moving_average(a, w=10):
    if len(a) < w:
        return a[:]
    return [val if idx < w else sum(a[(idx-w):idx])/w for idx,
                                                          val in enumerate(a)]


# 生产-1到1之间的100个数作为x
train_X = np.linspace(-1, 1, 100)
# y = 2x,并且加入噪声处理
train_Y = 2 * train_X + np.random.randn(*train_X.shape) * 0.3

plt.plot(train_X, train_Y, 'ro', label='Original data')
plt.legend()
plt.show()

# 创建模型
# 占位符，使用placeholder函数进行定义
# 代表x的输入
X = tf.placeholder("float")
# 代表x对应的真实值y
Y = tf.placeholder("float")
print(X)
print(Y)

# 模型参数
# 权重，被初始化为[-1,1]的随机数，形状为一维的数字
W = tf.Variable(tf.random_normal([1]), name="weigth")
print(W)
# 初始化为0，形状是一维的数字
b = tf.Variable(tf.zeros([1]), name="bias")
print(b)
# 向前结构
z = tf.multiply(X, W) + b
print(z)

# 反向优化
# 生成值与真实值的平方差
cost = tf.reduce_mean(tf.square(Y - z))
print(cost)
learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
print(optimizer)

# 训练模型

# 初始化所有变量
init = tf.global_variables_initializer()
# 定义参数
training_epochs = 20
display_step = 2

# 启动session
with tf.Session() as sess:
    sess.run(init)
    plotdata = {"batchsize": [], "loss": []}  # 存放批次值和损失值
    # 向模型中输入数据
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})
        # 显示训练中的详细信息
        if epoch % display_step == 0:
            loss = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
            print("Epoch:", epoch + 1, "cost=", loss, "W=", sess.run(W),
                  "b=", sess.run(b))
            if not (loss == "NA"):
                plotdata["batchsize"].append(epoch)
                plotdata["loss"].append(loss)
    print(" Finished! ")
    print("cost=", sess.run(cost, feed_dict={X: train_X, Y: train_Y}),
          "W=", sess.run(W), "b=", sess.run(b))

    # 图形显示
    plt.plot(train_X, train_Y, 'ro', label="Original data")
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label="Fittedline")
    plt.legend()
    plt.show()

    plotdata["avgloss"] = moving_average(plotdata["loss"])
    plt.figure(1)
    plt.subplot(211)
    plt.plot(plotdata["batchsize"], plotdata["avgloss"], "b--")
    plt.xlabel("Minibatch number")
    plt.ylabel("Loss")
    plt.title("Minibatch run vs. Training loss")
    plt.show()

    # 使用模型
    print("x=0.2, z=", sess.run(z, feed_dict={X: 0.2}))
