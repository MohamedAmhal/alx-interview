#!/usr/bin/python3
'''
the script for reading from a generator programmes
documentations!!
'''


import sys

line_counter = 0
dictio = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
file_size = 0


def functi():
    for k in dictio.keys():
        if dictio[k] != 0:
            print(k, ": ", dictio[k])


try:
    for line in sys.stdin:
        '''
        loop read line by line
        documentation !
        '''
        line_counter += 1
        liste = line.split(' ')
        if int(liste[7]) in dictio.keys():
            dictio[int(liste[7])] += 1
        else:
            pass
        b = ''
        for i in liste[8]:
            if (i != "\\" or i != 'n'):
                b = b + i
            else:
                pass
        file_size = file_size + int(b)

        if line_counter == 10:
            line_counter = 0
            print("File size: ", file_size)
            functi()
finally:
    print("File size: ", file_size)
    functi()
