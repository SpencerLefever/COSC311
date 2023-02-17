#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
"""

@author: slefever1

Draw an octogan
"""

def makeOctagon():
    length = 0
    while length < 2:
        print('Enter a length greater than 2: ')
        length = int(input())

#Top third of the octagon
    for i in range(1, length):
        for j in range(i,length):
            sys.stdout.write(' ')
        for k in range(((i-1)*2)+length):
            sys.stdout.write('*')
        print('')
        sys.stdout.flush()
#Middle third of octagon
    for i in range(1,length+1):
        for j in range(1,(length*2)+ length -1):
            sys.stdout.write('*')
        print('')
        sys.stdout.flush()
#Final third of octagon
    for i in range(1, length):
        for j in range(0,i):
            sys.stdout.write(' ')
        for k in range(((length-i-1)*2)+length):
            sys.stdout.write('*')
        print('')
        sys.stdout.flush()

makeOctagon()