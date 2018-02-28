s=input("enter a string")
c=('a','e','i','o','u')
l=[]
for i in s:
  if(i in c):
    continue
  else:
    l.append(i)
print(l)
