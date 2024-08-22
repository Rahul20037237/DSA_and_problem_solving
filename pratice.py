#Compact list
l1=[1,23,43,34,233,423]
for index,value in enumerate(l1):
    print(index,value)
# dict iteration
dict={
    'a':'this is a one[a]',
    'b':'this is a two[b]',
    'c':'this is a three[c]',
    'd':'this is a four[a]'
}
for key,value in dict.items():
    print(key,value)
#dict forloop
string='this a string'
my_dict={letter:0 for letter in string}
print(my_dict)
import tryalgo
from collections import Counter,defaultdict
# print(help(tryalgo.arithm))
print(Counter(string))
defaultdic_1=defaultdict(list)
#getting input
#1
import sys
input1,input2=map(int,sys.stdin.readline().split())
print("input1",input1,"input2",input2)
#2
import os
M=12*10
list1=list(map(int,os.read(0,M).split()))
print(list1)
#graph readin input
no_edges=int(input())
graph=defaultdict(dict)
for _ in range(no_edges):
    u,v,weight=input().split()
    graph[u][v]=int(weight)
print(graph)
# assert 
n=int(input())
assert n==10
print("yes")
#output format
intt=10
floatt=1.23154
precision=2
print("int :%d double:%.3f"%(intt,floatt))
print("int :{} double:{:.2f}".format(intt,floatt))
print(f"int :{intt} double:{floatt:.5f}")
print(f"int :{intt} double:{floatt:.{precision}f}")
