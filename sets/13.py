python_students = {}
java_students = {}
union=python_students+java_students
print(union)
print(python_students-java_students)
print(len(union))
if java_students.issuperset(python_students):
    print(True)