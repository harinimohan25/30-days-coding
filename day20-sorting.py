#!/bin/python3
import sys
n = int(input())
a=list(map(int,input().split(' ')))

total=0
for i in range(n-1):
    count=0
    for j in range(n-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]= a[j+1],a[j]
            count=count+1
    if count==0 :
         break;
    else :
         total=total+count


print("Array is sorted in %r swaps."%total) 
print("First Element: %r"%a[0])
print("Last Element: %r"%a[n-1])