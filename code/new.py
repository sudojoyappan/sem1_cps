c=0
total=0
while c<5:
    c=c+1
    x=float(input("student's mark:"))
    if x>=90:
        print("Grade A")
    elif x>=80:
        print("Grade B")
    elif x>=70:
        print("Grade C")
    elif x>=60:
        print("Grade D")
    elif x>=50:
        print("Grade E")
    elif x<50:
        print("Grade F")
    total+=x
percentage=total/5
print(percentage)