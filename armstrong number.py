n=int(input())
def armst(n):
  l=len(str(n))
  temp=n
  sum=0
  while(n>0):
    rem=n%10
    sum+=rem**l
    n=n//10
  if(temp==sum):
    return True
  else:
    return False
if(armst(n)):
    print(n,"is the armstrong number")
else:
    print(n,"is not a armstrong number")
