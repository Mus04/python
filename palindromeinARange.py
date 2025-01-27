n,m=int(input()),int(input())
print([i for i in range(n,m+1) if str(i)==str(i)[::-1]])
