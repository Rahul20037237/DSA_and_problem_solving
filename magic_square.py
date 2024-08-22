# M=len(s)*((len(s)*len(s)+1)/2)
n=3
i=int(n/2)
j=n-1
print(i,j)
magic=[]
magic.append([i,j])
# print(len(magic))
for k in range(0,10):
    print("step ",k)
    i=i-1
    j=j+1
    if [i,j] not in magic:
        if i==-1 and j==n:
            i=0
            j=n-2
            magic.append([i,j])
            print(i,j)
        elif i==-1 and j!=n:
            i=n-1
            print(i,j)
            magic.append([i,j])
        elif i!=-1 and j==n:
            j=0
            print(i,j)
            magic.append([i,j])
        else:
            print(i,j)
            magic.append([i,j])
    else:
        i=i+1
        j=j-2
        magic.append([i,j])
        print(i,j)        
