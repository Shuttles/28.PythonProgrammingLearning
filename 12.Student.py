#!/usr/bin/env python
# coding=utf-8

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("name = {0}, age = {1}".format(self.name, self.age))

stu1 = Student('jack_ma', 22)
stu2 = Student('Bob', 21)
stu1.show()
stu2.show()
print(type(Student))
print(type(stu1))
