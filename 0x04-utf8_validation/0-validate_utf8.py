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
    if (len(lis) == 1):
        if (lis[0] == 0):
            return True
        else:
            return False
    num = lis[0]
    if (num > 5):
        return False
    else:
        for i in range(1, len(lis)):
            if(lis[i] == 1):
                num -= 1
            else:
                break

        if (num == 1):
            return True
        else:
            return False
