con=int(input("Enter number of times you want to run calculator"))
x=0
while x<=con:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter another number:"))
    print("type +,-,*,/ for their respective operations")
    choice=input("Enter an operator:")
    if choice=="+":
        print("You have chosen addition")
        result=num1+num2
    elif choice=="-":
        print("You have chosen subtraction")
        result=num1-num2
    elif choice=="*":
        print("You have chosen multiplication")
        result=num1*num2
    elif choice=="/":
        print("You have chosen division")
        result=num1/num2
    else:   
        print("Invalid Operator")
    print(result)
    con+=1
