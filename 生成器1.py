#!/usr/bin/env python3
#antuor:Alan




def f():                                    #1     #4
    msg = yield 'first yield msg'                     #5      #8
    print ("generator inner receive:", msg)                     #9
    msg = yield 'second yield msg'                                  #10
    print ("generator inner receive:", msg)

g = f()                                       #2
msg = g.__next__()                              #3
print('generator outer receive:", msg')                  #6
msg = g.send('first send msg')                              #7
print('generator outer receive:", msg')                                 #11
g.send('second send msg')                                                   #12