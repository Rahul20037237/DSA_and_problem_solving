#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#
def matrixRotation(matrix, r):
    n=len(matrix)-1
    result=[[None]*n]*n
    print(result,n)
    for i in range(n):
        for j in range(n):
            if i==0:
                if i<=j:
                    result[i][j]=matrix[i+1][j]
                else:
                    result[i][j]=matrix[i][j+1]
            elif i==n:
                if i>=j:
                    result[i][j]=matrix[i-1][j]
                else:
                    result[i][j]=matrix[i][j-1]
    return result
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))
    print(matrix)
    print(matrixRotation(matrix, r))
