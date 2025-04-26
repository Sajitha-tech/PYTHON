str=input("Enter a string : ")
lst=set()

for char in str:
    if char not in lst:
        print(f"'{char}' appears {str.count(char)} times")
        lst.add(char)
    
