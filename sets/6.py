x={1, 3, 5, 7, 9, 11} 
flag6=False
flag7=False
flag11=False
flag0=False
for i in x:
    if i==6:
        flag6=True
    if i==7:
        flag7=True
    if i==11:
        flag11=True
    if i==0:
        flag0=True

if flag6==True:
    print(True)
else:
    print(False)
if flag7==True:
    print(True)
else:
    print(False)
if flag11==True:
    print(True)
else:
    print(False)
if flag0==True:
    print(True)
else:
    print(False)