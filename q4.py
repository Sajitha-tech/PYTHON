str=input("Enter a line : ")
w=str.split()
print(w)
new=set()
for i in w:
    if i not in new:
        print(f"The word '{i}' appears {w.count(i)} times")
        new.add(i)








