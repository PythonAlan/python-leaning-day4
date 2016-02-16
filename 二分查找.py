#!/usr/bin/env python3
#antuor:Alan

def num_search(data_source,find_n):
    mid = int(len(data_source)/2)
    if len(data_source)>1:
        if data_source[mid] > find_n:
            print("data in left of [%s]" % data_source[mid])
            num_search(data_source[:mid],find_n)              ###递归函数调用自身
        elif data_source[mid] < find_n:
            print("data in right of [%s]" % data_source[mid])
            num_search(data_source[mid:],find_n)
        else:
            print('found numbers:',data_source[mid])
    else:
        print('can not found')
if __name__ =="__main__":
    data = list(range(1,60000))
    print(data)
num_search(data,6750)