

n=input("enter the  elements : ")
s=n.split()
a=[]
for i in s:
    i=int(i)
    if i>100:
      a.append('over')
    else:
      a.append(i)
print(a)
