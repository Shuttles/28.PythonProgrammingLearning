#!/usr/bin/env python
# coding=utf-8

import math

'''
def circle(r):
    result = math.pi * r * r
    return result
r = float(input("请输入圆的半径："))
print("半径为%f的圆的面积是%f" % (r, circle(r)))
'''

r = float(input("请输入圆的半径："))
result = lambda r : math.pi * r * r
print("半径为%f的圆的面积是%f" % (r, result(r)))
