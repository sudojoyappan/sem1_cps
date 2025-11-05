l=[1,2,3,4,5,6]
k=int(input("Enter the shift value:"))
for i in range(k):
    x=l.pop(0)
    l.append(x)
print(l)
