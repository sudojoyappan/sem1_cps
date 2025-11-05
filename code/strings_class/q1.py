x=input("Enter a string:")
count=0
for i in x:
    if i.isnumeric():
        count+=1
print("Total numeric values=",count)
