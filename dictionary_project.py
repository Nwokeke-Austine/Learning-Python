#program to keep accepting input from user based on the number of students the user wants to input; name, level, department, age, sex. And store it

students = []
number_of_students = int(input("How many students: "))


for i in range(number_of_students):
    student = {}
    print("-----------------------------------------------------")
    print("Student", i+1)
    name = input("Enter Student's Name: ")
    department = input("Enter Student's Department: ")
    regno = input("Enter Registration Number: ")

    student = {
        "name": name,
        "department": department,
        "regno": regno,

    }

    students.append(student)

for s in students:
    print(s)
