a=int(input("enter limit : "))
f1=0
f2=1
print(f1)
print(f2)
i=2
while i<a:
    f3=f1 +f2
    f1=f2
    f2=f3
    i=i+1
    print(f3)
