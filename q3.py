x=[-1,-2,1,5,6,7,-9] 
y=['a','e','i','o','u','A','E','I','O','U']
l1=[]
l2=[]
l3=[]
print("list of positive integers : ")
for i in x:
   if i > 0:
      l1.append(i)
print(l1)
print("Square of n numbers:")
for i in x:
    c=i*i
    l2.append(c)
print(l2)

print("list of vowels from given word : ")
x="onion" 
for i in x:
    for j in y:
        if i==j:
          l3.append(i)
print(l3)
print("Ordinal value of each element")
for i in x:
    print(ord(i))        
      
    