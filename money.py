m=int(input())
n=m//10
m%=10
n+=m//5
m%=5
n+=m
print(n)