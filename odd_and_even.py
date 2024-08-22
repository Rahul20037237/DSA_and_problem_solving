import sys
def increment(n,incre):
    return n+incre
def Oddstream(n,i=1):
    if n==0:
        return 1
    else:
        print(i)
        i=increment(i,2)
        return Oddstream(n-1,i)
def Evenstream(n,i=0):
    if n==0:
        return 
    print(i)
    i=increment(i,2)
    return Evenstream(n-1,i)
def print_from_stream(n,stream):
    if stream=="odd":
        Oddstream(n)
    else:
        Evenstream(n)
n=int(input())
for i in range(n):
    stream,n=sys.stdin.readline().split()
    print_from_stream(int(n),stream)
    