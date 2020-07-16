#!/usr/bin/env python
# coding=utf-8
'''random模块'''

import random

#生成0~1之间的随机数
print(random.random())

#指定范围内的随机数
print(random.randint(10, 100))

#随机获取列表中的一个值
list1 = [1, 2, 3, 5, 7, 11]
print(random.choice(list1))
