#Algorithm for printing multiplication tables up to N
N=int(input("Enter a number:"))
i=1
while i<=N:
    j=1
    while j<=10:
        print(i*j,end=" ") 
        j+=1
    print("\n")
    i+=1