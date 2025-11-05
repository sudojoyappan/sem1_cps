start=1
centre=1
space=9
l='1234567890'
for i in range(1,11):
    length=centre
    for s in range(space):
        print(" ",end="")
    for j in range(length):
        f=l.find(str(start))
        print(l[f],end="")
        f+=1
    centre+=2
    start+=1
    space-=1
