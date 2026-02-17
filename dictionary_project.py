#program to keep accepting input from user based on the number of students the user wants to input; name, level, department, age, sex. And store it

students = []
number_of_students = int(input("How many students: "))


for i in range(number_of_students):
    student = {}

    print("Student", i+1)
    student["name"] = input("Enter Student's Name: ")
    student["department"] = input("Enter Student's Department: ")
    student["regno"] = input("Enter Registration Number: ")

    students.append(student)

for s in students:
    print(s)
