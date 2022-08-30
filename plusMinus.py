#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    tlen = len(arr)
    countp = 0
    countn = 0
    countz = 0
    for i in range(len(arr)):
        if arr[i]>0:
            countp +=1
        elif arr[i]<0:
            countn +=1
        elif arr[i]==0 :
            countz +=1
    print(format(countp/tlen,".6f"))
    print(format(countn/tlen,".6f"))
    print(format(countz/tlen,".6f"))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
