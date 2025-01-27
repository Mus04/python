#input string will be given only the starting and the last character should be printed and the remaining digits in the middle count should be printed
# example :ertyu
# output:e3u
s=input()
if(len(s)>10):
  print(s[0]+str(len(s)-2)+s[-1])
else:
  print(s)
