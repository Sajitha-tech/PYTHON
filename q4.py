l=[]
for i in range(32,100):
    sqr=i*i
    if 1000<=sqr<=9999 and all(int(n)%2==0 for n in str(sqr)):
                l.append(sqr)
print(l)

                
    


     
