#!/usr/bin/env python3
#antuor:Alan

'''装饰器的作用就是给已经实现的功能扩展新的功能'''
def login(func):                 #func = tv
    def inner(*args,**kwargs):              #把验证代码放第二层是防止未调用tv（）就开始验证
        print('user verification...')
        func(*args,**kwargs)                #func = tv
    return inner                 #只是返回一个内存地址


def home(name):
    print('welcome to %s home page' % name)

@login                           #装饰器，函数开始就先执行login
def tv(name,pwd = 123):
    print('welcome to %s tv page ' % name)
@login
def movie(name):
    print('welcome to %s movie page ' % name)

# tv = login(tv)
# page_name = 'asd'
tv('Alan',pwd = 123)
home('kobe')

