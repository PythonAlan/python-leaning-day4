#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#antuor:Alan

###1迭代器###
"""
python2.7调用next()方法 : print(names.next())
python3.x调用next()方法 : print(names.__next__())

当编程迭代器之后,只有一个next()方法,没有其它功能.
"""

###2最简单迭代器###
names = iter(['alan','kobe','yoyo','rain'])
print(names.__next__())
print(names.__next__())
print(names.__next__())
print(names.__next__())

###3for循环迭代###
"""
最简单python已经封装好的迭代形式,
f.readlines或者f.readline则会写入内存,速度慢
"""
f = open('test.txt')
for line in f:
    print(line)

###生成器###
"""
定义:如果一个函数调用时返回一个迭代器,那么这个函数就是生成器(generator),
如果函数包换yield语法,那么这个函数就是生成器.

能实现异步,提供中断的功能
"""
def cash_out(account):
    while account > 0:
        account -= 100
        yield 300
        print('提款')

ATM = cash_out(600)  ###查看这个函数的类型
print(type(ATM))     ###<class 'generator'>,返回一个迭代器
print(ATM.__next__())
print(ATM.__next__())
print(ATM.__next__())
print(ATM.__next__())








