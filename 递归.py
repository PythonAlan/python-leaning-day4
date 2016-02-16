#!/usr/bin/env python3
#antuor:Alan
'''斐波那契数列，最后一个数等于前两个数只和'''

def func(arg1,arg2,stop):
    if arg1 == 0:
        print(arg1,arg2)
    arg3 = arg1 + arg2
    print(arg3)
    if arg3<stop:    #必须明确规定结束条件，称为递归出口
        func(arg2,arg3,stop)

func(0,1,30)