# -*- coding:utf-8 -*-
from __future__ import print_function

'''
HelloWorld example using TensorFlow library.

Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

'''
简单  helloworld 使用 TensorFlow
创建一个常量 op
这个 op 作为节点被添加到默认图
这个值被创建者返回并显示在输出中
'''



import tensorflow as tf

# Simple hello world using TensorFlow

# Create a Constant op
# The op is added as a node to the default graph.
#
# The value returned by the constructor represents the output
# of the Constant op.
hello = tf.constant('Hello, TensorFlow!')

# Start tf session
sess = tf.Session()

# Run the op
print(sess.run(hello))

'''
输出内容：

Hello, TensorFlow!
'''
