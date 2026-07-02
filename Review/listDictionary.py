students = [
    {"Name": "Austine", "Score": 80},
    {"Name": "John", "Score": 55},
    {"Name": "Mary", "Score": 92},
    {"Name": "David", "Score": 48},
    {"Name": "Grace", "Score": 76}
]

#print names of students who passed above 50
studentpassed = 0
for student in students:
    if student["Score"] >= 50:
        studentpassed += 1
        print(student["Name"])

print(f"Number of students that passed: {studentpassed}")

