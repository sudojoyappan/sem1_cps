start=1#type:ignore
centre=1
space=9
l='01234567890123456789'
for i in range(1,11):
    for s in range(space):
        print(" ",end="")
    if centre<=9:
        newl=l[start:centre]
        print(newl,end='')
        print(centre,end='')
        print(newl[::-1],end='')
        print()
    else:
        newl=l[start:centre]
        print(newl,end='')
        #print(centre,end='')
        print(int(str(centre)[1]),end='')
        print(newl[::-1],end='')
        print()
    centre+=2
    start+=1
    space-=1
