import math
def odd_or_even(a):
  if a==0:
    return "the given number is a prime number"
  for i in range(2,int(math.sqrt(a))+1):
    if a%i ==0:
      return "the given number is a prime number"
a=int(input())
print(odd_or_even(a))
