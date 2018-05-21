s=input("enter a string")
c=('a','e','i','o','u')
l=[]
for i in s:
  if(i in c):
    continue
  else:
    l.append(i)
a=l[::-1]
a="".join(a)
print(a)
