#Algorithm for printing multiplication tables up to N
N=int(input("Enter a number:"))
for i in range(1,N+1):
    for j in range(1,11):
        print(i*j,end=" ")
    print("\n")