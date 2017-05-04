#!/bin/python

import sys
first=0
second=0
cnt=0
n = int(raw_input().strip())
bin_n = "{0:b}".format(n)
print len(max(bin_n.split('0')))
        
    