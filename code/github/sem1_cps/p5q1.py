x=list(eval(input("Enter the valeus of the list")))
max=0
min=0
for i in x:
    if i>max:
        max=i
for i in x:
    if i<min:
        min=i
print(min,max)