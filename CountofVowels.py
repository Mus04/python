#count of vowels in even and odd positions
s=input()
s1=s[::2]
s2=s[1::2]
ec=s1.count("a")+s1.count("e")+s1.count("i")+s1.count("o")+s1.count("u")
oc=s2.count("a")+s2.count("e")+s2.count("i")+s2.count("o")+s2.count("u")
print(f"even count {ec} ,odd count {oc}")
