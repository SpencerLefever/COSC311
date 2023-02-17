#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: slefever1

Triangular Number Sequence

1. Print first 20 numbers of triangular sequence
2. Calculate and output the sum of even numbers and sum of
   odd numbers in the first 20 numbers
"""
triSeq = 0
oddSum = 0
evenSum = 0
for i in range(1,21):
    triSeq = triSeq + i
    print(triSeq)
    if triSeq%2 == 0:
        evenSum = evenSum + triSeq
    else:
        oddSum = oddSum + triSeq

print('Even sum: ', evenSum)
print('Odd sum: ', oddSum)

