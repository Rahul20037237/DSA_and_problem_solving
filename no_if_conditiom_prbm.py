import sys
from collections import defaultdict
n,m=map(int,sys.stdin.readline().split())
Matrix=[]
answer=list
for i in range(n):
    str_1=sys.stdin.readline().split()
    Matrix.append(str_1)
print(Matrix)