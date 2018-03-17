n=input("enter string")
a=[]
for i in n:
  if(i.isdigit()):
    a.append(i)
print("".join(n for n in a))
