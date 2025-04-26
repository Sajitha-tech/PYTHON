str=input("Enter a string : ")
a=str.split()
count=0 
for i in a: 
   count+=i.count('a')+i.count('A') 
print("The number of occurence of a : ",count)
