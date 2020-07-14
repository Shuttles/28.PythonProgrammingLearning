#!/usr/bin/env python
# coding=utf-8

fp = open("./input", "r+")
print("文件名：", fp.name)

str = 'www.haizeix.com'
fp.seek(0, 2) #表示文件指针移动到./input结尾位置

line = fp.write(str)

#读取文件所有内容
fp.seek(0) #设置文件指针到开头
for index in range(3):
    line = next(fp)
    print("文件行号：%d - %s" % (index, line))

fp.close()

