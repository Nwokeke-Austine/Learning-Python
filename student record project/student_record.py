# Collect student data
# Store in list
# Print data
# Add grade function
# Add statistics

#How many students you want to register
num_of_students = int(input("Enter number of students you want to register: "))

students_list = []

#grade function
def calculate_grade(score):
    if score >= 70:
        return("A")
    elif score >= 60:
        return("B")
    elif score >= 50:
        return("C")
    elif score >= 45:
        return("D")
    elif score >= 40:
        return("E")
    else:
        return("F")
    
for i in range(num_of_students):
    print("-----------------------------------------")
    print(f"------ STUDENT {1 + i} ------")
    name = input("Enter name of student: ")
    department = input("Enter department of student: ")
    regno = input("Enter registration number: ")
    level = int(input("Enter Level: "))
    while True:
        score = int(input("Student Score: "))
        if 0 <= score <= 100:
            break
        print("Invalid score! Please enter a number between 0 and 100.")
    grade = calculate_grade(score)

    student = {
    "Name" : name,
    "Department" : department,
    "Registration Number" : regno,
    "Level" : level,
    "Score" : score, 
    "Grade" : grade
}
    
    students_list.append(student)

print("\n------ STUDENT RECORDS ------")

for student in students_list:
    print("---------------------------")
    for key, value in student.items():
        print(f"{key}: {value}")

highest_score = students_list[0]["Score"]
lowest_score = students_list[0]["Score"]
total_score = 0

for student in students_list:
    score = student["Score"]
    total_score += score
    if score > highest_score:
        highest_score = score
    if score < lowest_score:
        lowest_score = score

average_score = total_score/len(students_list)

print("\n-----STATISTICS-----")
print(f"Higest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Class Average: {average_score}")
        
