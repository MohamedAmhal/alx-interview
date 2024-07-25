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
    if (len(data) == 0):
        return False
    i = 0
    while(i < len(data)):
        a = bits(data[i])
        comp = 0
        for j in a:
            if int(j) == 1:
                comp += 1
            else:
                break

        if (len(data) == 1 and comp == 1):
            return False
        if (comp == 0):
            i = i + 1
            continue
        elif (comp == 1):
            return False
        if (comp > 4):
            return False
        else:
            i = i + 1
            for j in range(comp - 1):
                if (i >= len(data)):
                    return False
                b = bits(data[i])
                if (int(b[0]) == 1 and int(b[1]) == 0):
                    i = i + 1
                else:
                    return False

    return True
