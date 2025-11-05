x=list(eval(input("Enter values of list:")))
print(x)
y=x[::-1]
if x==y:
    print(x,"is a palindrome list")
else:
    print(x,"is not a palindrome list")
