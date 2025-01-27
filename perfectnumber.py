n=int(input())
def perf(n):
  summ=0
  for i in range(1,n):
    if(n%i==0):
      summ+=i
  if(summ==n):
    print(n,"is a perfect number")
perf(n)
