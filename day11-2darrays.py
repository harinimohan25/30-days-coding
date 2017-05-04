#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

max = -100
for i in range(4):
    for j in range(4):
        sum = arr[i+1][j+1]
        for x in range(3):
            sum += arr[i][j+x] + arr[i+2][j+x]
        if sum > max:
            max = sum              
print(max)