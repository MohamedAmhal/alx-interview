#!/usr/bin/python3
'''
doc doc doc dc dki
dnjfkfkf
fjflkgn
'''


def bits(a):
    '''
    doc doc doc dc dki
    dnjfkfkf
    fjflkgn
    '''
    b = ""
    while(a != 0):
        b = str(a % 2) + b
        a = a // 2

    while(len(b) < 8):
        b = '0' + b

    return b


def validUTF8(data):
    '''
    doc doc doc dc dki
    dnjfkfkf
    fjflkgn
    '''
    lis = []
    for i in range(len(data)):
        comp = 0
        a = bits(data[i])
        for j in a:
            if int(j) == 1:
                comp += 1
            else:
                break
        lis.append(comp)
        comp = 0
    bol = 0
    for i in range(len(lis) - 1):
        if (lis[i] == (lis[i + 1] + 1)):
            pass
        elif (lis[i] == lis[i + 1]):
            pass
        else:
            bol = 1

    if (bol == 0):
        return True
    else:
        return False
