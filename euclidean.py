def euclidean(a,b):
    if b==0:
        return a
    a_=a%b
    return euclidean(b,a_)
a,b=map(int,input().strip().split())    
print(int((a*b)/euclidean(a,b)))