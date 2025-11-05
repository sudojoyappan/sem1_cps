x=list(eval(input("Enter values of list:")))
y=['a','b','c','d','e']
z=[]
l1=len(x)
l2=len(y)
if l1>l2:
    l=l1
else:
    l=l2
for i in range(l):
    z.append(x[i])
    z.append(y[i])
print(z)