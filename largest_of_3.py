#Algorithm for finding the largest of three numbers
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
z=int(input("Enter a number:"))
if x>z and x>y:
    print(x,"is greatest") 
elif y>x and y>z:
    print(y,"is greatest")
else:
    print(z,"is greatest")