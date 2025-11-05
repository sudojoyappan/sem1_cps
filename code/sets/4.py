num1 =  {1, 2, 3, 4, 5, 7}
num2 =  {2, 4}
num3 =  {2, 4}
if num1.issuperset(num2):
    print(True)
else:
    print(False)
if num2.issuperset(num3):
    print(True)
else:
    print(False)
if num3.issuperset(num2):
    print(True)
else:
    print(False)
