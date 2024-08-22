n=int(input())
numbers=list(map(int,input().strip().split()))
# LEXI=[tuple(i) for i in numbers]
# LEXI.sort(key=len)
# LEXI.sort(key=lambda x:x[0],reverse=True)
# LEXI=["".join(i) for i in LEXI]
# # maxi=""
# # for i in LEXI:
# #     maxi+=i
# # print(int(maxi))
# print(LEXI)
numbers.sort()
LEXI=[tuple(str(i)) for i in numbers]
LEXI.sort(key=lambda x:x[0],reverse=False)
print(LEXI)