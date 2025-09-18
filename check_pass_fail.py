#Algorithm for checking if a student passes or fails in an exam
marks=float(input("Enter marks:"))
passing_marks=float(input("Enter pass marks:"))
if marks>=passing_marks:
    print("Pass")
else: 
    print("Fail")