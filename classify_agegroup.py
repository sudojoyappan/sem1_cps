#Algorithm for classifying a person’s age group
age=int(input("Enter age of person:"))
if age<18:
    if age<13:
        print("Child")
    else:
        print("Teenager")
else:
    if age<60: 
        print("Adult")
    else:
        print("Senior")