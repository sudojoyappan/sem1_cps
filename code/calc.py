def calc():
    x=float(input("Enter first number:"))
    y=float(input("Enter 2nd number:"))
    o=input("Enter arithmetic operator:")
    z=0
    if o=="+":
        z=x+y
    elif o=="-":
        z=x-y
    elif o=="*":
        z=x*y
    elif o=="/":
        z=x/y
    else:
        print("Invalid input")
    
    print(z)

calc()