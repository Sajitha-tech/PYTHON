l1=[1,3,5,6]
l2=[3,9,2,7]
print(l1)
print(l2)
print('Result from Entered Lists : ')
if len(l1)==len(l2):
      print("Have same length")
else:
      print("Doesnt have same length")
  
if sum(l1)==sum(l2):
      print("sum if list is same")
else:
      print("sum if list is  not same")
common=set(l1)&set(l2)
if common:
      print(common)
else:
      print("No common values")

 
  
