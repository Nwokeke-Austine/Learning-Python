# Collect student data
# Store in list
# Print data
# Add grade function
# Add statistics

#How many students you want to register
num_of_students = int(input("Enter number of students you want to register: "))

students_list = []


for i in range(num_of_students):
    print("-----------------------------------------")
    print(f"------ Student {1 + i} ------")
    name = input("Enter name of student: ")
    department = input("Enter department of student: ")
    regno = input("Enter registration number: ")
    level = input("Enter Level: ")
    score = int(input("Student Score: "))

    student = {
    "Name" : name,
    "Department" : department,
    "Registration Number" : regno,
    "Level" : level,
    "Score" : score    
}
    
    students_list.append(student)

print("\n------ STUDENT RECORDS ------")

for student in students_list:
    print("---------------------------")
    print("Name:", student["Name"])
    print("Department:", student["Department"])
    print("Registration Number:", student["Registration Number"])
    print("Level:", student["Level"])
    print("Score:", student["Score"])