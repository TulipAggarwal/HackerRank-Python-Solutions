#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    tlen = len(arr)
    smax = 0
    smin = 0
    for i in range(1,tlen):
        smax += arr[i]
    for i in range(0,tlen-1):
        smin += arr[i]
    print(smin,smax)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
