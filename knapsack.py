def knap(n,sack,value,d_list):
    total_amount=0
    while (sack>0):
        if len(value)==0:
            break
        max=value.pop()
        sack_value=d_list[max]
        min_s=min(sack,sack_value[1])
        total_amount=total_amount+min_s*(sack_value[0]/sack_value[1])
        sack=sack-min_s
    return total_amount
n,sack=map(int,input().strip().split())
d_list=dict()
value=[]
for _ in range(n):
    n1,n2=map(float,input().strip().split())
    v=n1/n2
    d_list[v]=[n1,n2]
    value.append(v)
value=sorted(value)
print(knap(n,sack,value,d_list))