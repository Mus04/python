s=input()
c=[s.count("a"),s.count("e"),s.count("i"),s.count("o"),s.count("u")]
print(c)
s1=[]
for i in range(len(c)):
  r=c[i]%2
  if(r!=0):
    s1.append(s[i])
print(min(s1))
  
