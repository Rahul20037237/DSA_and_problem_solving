def fk(kp,p):
   W=0
   total_cost=0
   for i in range(len(p)):
      if kp!=0:
         a=min(W,)
         total_cost=int(p[i][0]/p[i][1])+total_cost
         print(total_cost)
      else:
         break
   return total_cost

n,kp=map(int,input().strip().split())
product=[list(map(int,input().strip().split())) for i in range(n)]
print(fk(kp,product))