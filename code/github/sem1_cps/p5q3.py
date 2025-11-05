x=list(eval(input("Enter the values of the list:")))
y=int(input("Enter value you want to check is present in the list"))
flag=False
count=0
for i in x:
    if i==y:
        flag=True
        count+=1
if flag==True:
    print(y,"occurs in the list and it occurs",count,"times")