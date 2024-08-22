def multiply(a,b):
    return [[a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]]
def mat_exp(n):
    result=[[1,0],[0,1]]
    matrix=[[1,1],[1,0]]
    for i in range(n):
       if n<=0:
           break
       if  n%2==1:
            result=multiply(result,matrix)
       matrix=multiply(matrix,matrix)
       n//=2
    return ((result[0][0]-1)**2)
n=int(input())
if n<=2:
        print(n)
else:
    print(mat_exp(n))