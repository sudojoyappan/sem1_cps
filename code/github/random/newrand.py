n=10
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        print((i+j)%10,end="")
    for k in range(i-2,-1,-1):
        print((k+i)%10,end="")
    print() 