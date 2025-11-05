s1=input("Enter a string:")
sum=0
count=0
for i in s1:
    if i.isnumeric():
        sum+=i
        count+=1
print("Sum is:",sum)
print("Average is:",sum/count)
