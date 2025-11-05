s=input("Enter a string:")
for i in s:
    if i.isalnum():
        print(i,end="")
    else:
        print("#",end="")
