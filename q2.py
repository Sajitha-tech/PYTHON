i=int(input("Enter the Current year : "))
x=int(input("Enter the Last year : "))
while i <= x:
 if (i % 4 ==0) or (i % 100 !=0) and (i % 400 ==0): 
   print(i)
 i+=1
