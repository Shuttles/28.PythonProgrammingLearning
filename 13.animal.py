#!/usr/bin/env python
# coding=utf-8

'''类的继承'''

#父类，又称基类
class Animal(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print("{} run...".format(self.name))

#子类，又称派生类
class Cat(Animal):
    def __init__(self, name, color):
        #调用父类的方法
        super().__init__(name)
        self.color = color

    def show(self):
        print("name = {}, color = {}".format(self.name, self.color))

#子类
class Dog(Animal):
    def run(self):
        print("{} run fast.".format(self.name))

#创建对象
cat = Cat('喵喵', '小白')

#调用方法
cat.run()
cat.show()

dog = Dog('Honey')
dog.run()
