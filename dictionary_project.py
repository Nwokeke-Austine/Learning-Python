#program to keep accepting input from user based on the number of students the user wants to input; name, level, department, age, sex. And store it

number_of_students = int(input("How many students: "))

for i in range(number_of_students):
    print("student", i+1)

    student = input("Enter name of student: ")

print (student)

student_name = { }

