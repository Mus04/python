n=int(input())
def strongnum(n):
  temp=n
  sum=0
  while(n>0):
    rem=n%10
    sum+=factorial(rem)
    n=n//10
  if(temp==rem):
    return True
  else:
    return False
def factorial(n):
  fact=1
  for i in range(1,n+1):
    fact*=i
    return fact
if(strongnum(n)):
  print(n,"is a strong number")
else:
  print(n,"is not a strong number")
