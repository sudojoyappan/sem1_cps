x= {'mango', 'apple'}
y= {'mango', 'orange'}
z= {'mango'}
if x.issubset(y):
    print(True)
else:
    print(False)
if y.issubset(x):
    print(True)
else:
    print(False)
if y.issubset(z):
    print(True)
else:
    print(False)
if z.issubset(y):
    print(True)
else:
    print(False)