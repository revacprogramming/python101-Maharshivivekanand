#to find averge of numbers until you enter exit
i=1
sum=0
count=0
while(i>=0):
    c=input("enter the numbers ")
    if c =="exit":
        break
    else:
     sum=sum+float(c)
     i=i+1
     count=count+1
avg=sum/count
print(count) #to know the number of numbers added before entering exit
print("averge of the numbers ",avg)
print("sum of the numbers ",sum)